# AICW-PROJECT

# 🏥 MedAI: Multi-Disease Diagnostic System
MedAI is an AI-powered healthcare diagnostic platform designed to provide fast, accessible, and easy-to-understand medical scan analysis. It combines the power of Computer Vision for disease detection and Generative AI (LLMs) for clinical reporting.

## 📝 Problem Statement
Traditional medical diagnostic processes can be time-consuming, and patients often struggle to understand complex radiological reports. There is a need for a system that can:
Provide instant preliminary analysis of medical images.
Bridge the language barrier for non-English speaking patients (specifically Telugu).
Offer an easy-to-use interface for maintaining patient history.

## 🚀 Solution Approach
Image Classification: Used Convolutional Neural Networks (CNNs) and Transfer Learning to classify Brain Tumors, Pneumonia, Retina diseases, and Skin Cancer.Clinical Analysis: Integrated Groq (Llama 3.3) to generate detailed medical reports based on AI predictions.
Bilingual Support: Developed a system to provide reports in both English and Telugu.
Voice Integration: Used gTTS to convert the Telugu analysis into speech for better accessibility.
Data Management: Implemented SQLite for secure user authentication and historical record keeping.

## ✨ Project Features
Multi-Disease Detection: Brain Tumor, Pneumonia, Retina, and Skin Cancer analysis.
Detailed Clinical Reports: Professional insights using LLMs.
Bilingual Analysis: Native Telugu support for reports.
Audio Report: Listen to the diagnostic report in Telugu.

## 📂 Folder Structure


Real_Medical_AI/
├── models/               # Pre-trained .h5 files
├── static/
│   ├── uploads/          # Saved images and generated audio files             
├── templates/            # HTML files (Login, Register, Dashboard, Results, History)
├── app.py                # Main Flask Application
├── .env                  # Environment variables (API Keys)
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation

Patient History: Securely store and view previous analysis results.
Secure Authentication: User login and registration system.

## 📄 File Descriptions
app.py: The core engine handling routing, model inference, and API integrations.
models/: Contains the deep learning models trained on medical datasets.
templates/: Jinja2 templates for the web front-end.
users.db: SQLite database storing user credentials and patient history.

## 🛠️ Steps to Run the Project
1.Clone the Repository
git clone (https://github.com/sivaparvathi620/AICW-PROJECT.git)
cd AuraScan

2.Install Dependencies
pip install -r requirements.txt

3.Set Up API Key: Create a .env file and add your Groq API Key
GROQ_API_KEY=your_actual_api_key_here

4.Run the Application
python app.py

