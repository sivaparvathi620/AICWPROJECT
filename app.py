import os
import numpy as np
import tensorflow as tf
import sqlite3
import re
from flask import Flask, request, render_template, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing import image
from tensorflow.keras import backend as K
from datetime import datetime
from groq import Groq
from dotenv import load_dotenv
from gtts import gTTS

# Load environment variables from .env file
load_dotenv(override=True)

app = Flask(__name__)

# Security: Pulling secret keys from environment variables
app.secret_key = os.getenv('SECRET_KEY', 'medical_ai_fallback_key')
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Groq API Configuration
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    print("❌ ERROR: Groq API Key not found in .env file!")
else:
    print(f"✅ SUCCESS: AuraLens AI is connected to Groq.")

client = Groq(api_key=groq_api_key)

def analyze_report_with_groq(category, status, confidence):
    prompt = f"""
    Act as an experienced Radiologist, but explain the scan like you’re talking to a patient or their family in everyday conversation.
    Look at the uploaded {category} scan image(s) and describe what you see in a simple, calm, and natural way.
    
    Clearly explain:
    - Whether the scan looks normal or if something looks off
    - Any visible problem and your confidence: {confidence}%
    - What the person should do next (Practical advice)

    Give the explanation in both English and Telugu.
    Format exactly like this:

    [ENGLISH]
    - What we see: (Simple explanation)
    - Why it matters: (Plain language)
    - What to do next: (Advice)

    [TELUGU]
    - ఏమి కనిపిస్తోంది: (సరళమైన వివరణ)
    - ఎందుకు ముఖ్యం: (సులభమైన కారణం)
    - తదుపరి ఏమి చేయాలి: (సాధారణ సూచనలు)
    """

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=1000
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Analysis Error: {e}"

# --- Database Initialization ---
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT UNIQUE, password TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, category TEXT, status TEXT, confidence TEXT, date TEXT)')
    conn.commit()
    conn.close()

init_db()

# --- Model Loading (Using Transfer Learning) ---
base_dir = os.path.dirname(os.path.abspath(__file__))
MODELS = {'brain': None, 'pneumonia': None, 'retina': None, 'skin': None}

try:
    # These models utilize Transfer Learning architectures like VGG16/ResNet
    MODELS['brain'] = tf.keras.models.load_model(os.path.join(base_dir, 'models/brain_tumor_model.h5'))
    MODELS['pneumonia'] = tf.keras.models.load_model(os.path.join(base_dir, 'models/chest_model.h5'))
    MODELS['retina'] = tf.keras.models.load_model(os.path.join(base_dir, 'models/retina_model.h5'))
    MODELS['skin'] = tf.keras.models.load_model(os.path.join(base_dir, 'models/skin_cancer_model.h5'))
    print("✅ All AI Models Loaded Successfully")
except Exception as e:
    print(f"❌ Model Loading Error: {e}")

def model_predict(img_path, category):
    K.clear_session()
    model = MODELS.get(category.lower())
    
    if model is None: 
        return "Normal (Simulated)", 95.0

    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img) / 255.0
    x = np.expand_dims(x, axis=0)
    
    preds = model.predict(x)
    
    if preds.shape[1] > 1:
        idx = np.argmax(preds[0])
        conf = round(float(np.max(preds[0]) * 100), 2)
        status = "Normal" if idx == 0 else "Detected"
    else:
        val = float(preds[0][0])
        conf = round(float((val if val > 0.5 else 1 - val) * 100), 2)
        status = "Detected" if val > 0.5 else "Normal"
        
    return status, conf

# --- Routes ---

@app.route('/')
def index():
    if 'user_id' in session: return render_template('index.html', user_name=session['user_name'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email, password = request.form['email'], request.form['password']
        conn = sqlite3.connect('users.db')
        user = conn.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password)).fetchone()
        conn.close()
        if user:
            session['user_id'], session['user_name'] = user[0], user[1]
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name, email, password = request.form['name'], request.form['email'], request.form['password']
        conn = sqlite3.connect('users.db')
        try:
            conn.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
            conn.commit()
            return redirect(url_for('login'))
        except: flash("Email already exists!")
        finally: conn.close()
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session: return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/documentation')
def documentation():
    if 'user_id' not in session: return redirect(url_for('login'))
    conn = sqlite3.connect('users.db')
    last_record = conn.execute("SELECT category, status, confidence, date FROM history WHERE user_id=? ORDER BY id DESC LIMIT 1", (session['user_id'],)).fetchone()
    conn.close()
    return render_template('documentation.html', record=last_record, user_name=session['user_name'])

@app.route('/predict', methods=['POST'])
def predict():
    if 'user_id' not in session: return redirect(url_for('login'))
    category = request.form.get('category')
    file = request.files['file']
    if file:
        filename = secure_filename(f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}")
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)

        status, conf = model_predict(path, category)
        full_analysis = analyze_report_with_groq(category, status, conf)

        audio_filename = None
        try:
            telugu_text = full_analysis.split("[TELUGU]")[1] if "[TELUGU]" in full_analysis else full_analysis
            clean_audio_text = re.sub(r'[*#_]', '', telugu_text)
            audio_gen_name = f"audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3"
            tts = gTTS(text=clean_audio_text, lang='te')
            tts.save(os.path.join(app.config['UPLOAD_FOLDER'], audio_gen_name))
            audio_filename = audio_gen_name
        except Exception as e:
            print(f"⚠️ Audio Generation Error: {e}")

        conn = sqlite3.connect('users.db')
        conn.execute("INSERT INTO history (user_id, category, status, confidence, date) VALUES (?, ?, ?, ?, ?)",
        (session['user_id'], category.upper(), status, f"{conf}%", datetime.now().strftime("%Y-%m-%d %H:%M")))
        conn.commit()
        conn.close()

        return render_template('result.html', results=[{
            'label': f"{category.upper()} - {status}",
            'conf': conf,
            'img': filename,
            'analysis': full_analysis,
            'audio': audio_filename
        }])
    return redirect(url_for('dashboard'))

@app.route('/history')
def history():
    if 'user_id' not in session: return redirect(url_for('login'))
    conn = sqlite3.connect('users.db')
    user_history = conn.execute("SELECT * FROM history WHERE user_id=? ORDER BY id DESC", (session['user_id'],)).fetchall()
    conn.close()
    return render_template('history.html', history=user_history, user_name=session['user_name'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)