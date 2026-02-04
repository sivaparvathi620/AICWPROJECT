# AICWPROJECT

# 🏥 AuraLens AI - MediGuide AI
MediGuide AI is an advanced medical diagnostic platform powered by Convolutional Neural Networks (CNN) to provide high-confidence screening for radiology and ophthalmology scans. The platform supports multiple languages including English and Telugu for better clinical accessibility.

# 📋 Project Problem Statement
Accurate and timely diagnosis is critical in healthcare, yet many regions face a shortage of specialist radiologists and ophthalmologists. Manual screening of MRI, X-ray, and Retina scans can be time-consuming and prone to human error, especially in high-volume environments. There is a need for an automated, AI-driven tool that can assist medical professionals by providing instant, reliable diagnostic analysis.

# 💡 Solution Approach
To solve this, we developed a multi-module AI system:

Deep Learning Models: Developed using TensorFlow/Keras, utilizing CNN architectures optimized for medical image classification.

Multimodal Categories: Specialized models for Brain MRI (Tumor), Chest X-Ray (Pneumonia), Retina Scans (Diabetic Retinopathy), and Skin Cancer.

User-Friendly Interface: A Flask-based web dashboard that allows healthcare providers to easily upload scans and receive immediate feedback.

Localized Reporting: Analysis outputs are designed to be accessible, supporting regional language context where necessary.

# ✨ Project Features
Multi-Diagnostic Support: Four distinct modules for different medical fields.

Real-time Analysis: Get AI-driven results in seconds after uploading.

Modern UI/UX: A sleek, dark-themed dashboard with Glassmorphism design.

Secure Portal: Individual login and registration system for patient data security.

History Logs: Track and view previous diagnostic reports.

# 📂 Folder Structure
Plaintext
AICW-PROJECT/
├── static/
│   ├── css/          # Custom styling (style.css)
│   ├── images/       # Icons and UI assets
│   └── uploads/      # Temporary storage for uploaded scans
├── templates/
│   ├── index.html    # Landing page
│   ├── login.html    # Authentication page
│   ├── register.html # Registration page
│   └── dashboard.html# AI analysis portal
├── models/           # Pre-trained .h5 or .keras files
├── app.py            # Main Flask application logic
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
# 📄 File Descriptions
app.py: The core engine of the project that handles routing and model predictions.

dashboard.html: The main user interface where users interact with the AI modules.

style.css: Contains the styling for the modern dark-mode aesthetic and blue glow effects.

requirements.txt: Lists all Python libraries needed (Flask, TensorFlow, NumPy, etc.).

# 🚀 Steps to Run the Project
Clone the Repository:

Bash
git clone https://github.com/your-username/AICW-PROJECT.git
cd AICW-PROJECT
Create a Virtual Environment:

Bash
python -m venv venv
venv\Scripts\activate   # For Windows
Install Dependencies:

Bash
pip install -r requirements.txt
Run the Application:

Bash
python app.py
Access the Dashboard: Open your browser and go to http://127.0.0.1:5000

## 📸 Project Screenshots

### Register Page
<img width="901" height="846" alt="image" src="https://github.com/user-attachments/assets/32f83780-aa60-4b3e-b68a-94d42c52b6ca" />

### Login Page
<img width="946" height="860" alt="image" src="https://github.com/user-attachments/assets/531f0620-fab5-40f3-9feb-d8de1a5a6116" />

### Home Page
<img width="1600" height="651" alt="image" src="https://github.com/user-attachments/assets/d94f19f3-c270-48ec-b2d2-ed1d8c8b37df" />
<img width="1600" height="408" alt="image" src="https://github.com/user-attachments/assets/4cc04c57-733e-4b0c-814e-ccef0d48bf39" />


### 🖥️ Analysis Dashboard
<img width="1362" height="886" alt="image" src="https://github.com/user-attachments/assets/5ade469b-ebf1-4916-9eef-95b733f3d1b6" />

### History Page
<img width="1600" height="625" alt="image" src="https://github.com/user-attachments/assets/253d5f72-a0ba-4f2d-935f-6f8053d01375" />


### 📊 AI Diagnostic Result
<img width="1600" height="873" alt="image" src="https://github.com/user-attachments/assets/114396a8-0371-4a18-9a81-f46969a3dce4" />
<img width="1600" height="619" alt="image" src="https://github.com/user-attachments/assets/26ec6eaf-f2fb-4f11-91ed-c4251c1f6b6c" />

### Download The PPT
<img width="1600" height="774" alt="image" src="https://github.com/user-attachments/assets/748aa2e8-d301-4624-b536-b0ad4c5c51b0" />

### Previous Latest Doc
<img width="1371" height="873" alt="image" src="https://github.com/user-attachments/assets/40f9349e-8889-4fb5-a105-cc18818c4f74" />

👨‍💻 Developed by
This is Team Project for AICW - AI Medical Diagnostic Center

1.M.SIVA PARVATHI
2.G.H.S.DEEPTHI
3.S.ASHA PRIYANKA
4.B.ROSHINI
