import os

class Config:
    BRAIN_MODEL_PATH = 'models/braintumor_model.h5'
    PNEUMONIA_MODEL_PATH = 'models/pneumonia_model.h5'
    UPLOAD_FOLDER = 'static/uploads'
    AUDIO_FOLDER = 'static/audio'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}