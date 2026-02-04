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

👨‍💻 Developed by
[Your Name / Team Name] Project for AICW - AI Medical Diagnostic Center
