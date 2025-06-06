import os
import json
import numpy as np
import tensorflow as tf
import streamlit as st
import pandas as pd
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import DepthwiseConv2D as OriginalDepthwiseConv2D
from googletrans import Translator
from deep_translator import GoogleTranslator

# Custom CSS Styling for PlantGuard App
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
            background-color: #F0F8FF;
        }

        .title {
            text-align: center;
            font-size: 55px;
            font-weight: 800;
            background: -webkit-linear-gradient(45deg, #43A047, #FFD54F);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }

        .section-title {
            font-size: 26px;
            color: #FF7043;
            font-weight: 700;
            margin-top: 30px;
            margin-bottom: 12px;
        }

        .card {
            background: linear-gradient(135deg, #FFFFFF 0%, #E3F2FD 100%);
            padding: 25px;
            border-radius: 20px;
            box-shadow: 0 6px 12px rgba(34, 34, 34, 0.15);
            margin-top: 20px;
        }

        .upload-box {
            background: #FFFDE7;
            padding: 20px;
            border: 2px dashed #FFEB3B;
            border-radius: 15px;
            text-align: center;
        }

        .stButton>button {
            background-image: linear-gradient(to right, #43A047, #FFEB3B);
            color: #333;
            border: none;
            padding: 0.7em 2em;
            border-radius: 10px;
            font-size: 18px;
            font-weight: 600;
            margin-top: 10px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .stButton>button:hover {
            background-image: linear-gradient(to right, #388E3C, #FFC107);
            color: white;
        }

        .footer {
            text-align: center;
            font-size: 13px;
            color: #777;
            margin-top: 60px;
        }

        .prediction {
            font-size: 22px;
            font-weight: 600;
            color: #2E7D32;
        }

        .confidence {
            font-size: 18px;
            color: #616161;
        }
    </style>
""", unsafe_allow_html=True)

# Logo Title Block
st.markdown("""
<div style="text-align:center; margin-bottom: 30px;">
    <span style="font-size:60px;">🌱</span>
    <span style="font-size:55px; font-weight:800; background: -webkit-linear-gradient(45deg, #43A047, #FFEB3B);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;">PlantGuard</span>
    <br>
    <span style="font-size:18px; color:#555;">AI-Powered Plant Disease Detection</span>
</div>
""", unsafe_allow_html=True)

# Set up paths
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize translator
translator = Translator()

# Custom DepthwiseConv2D to handle model loading
class CustomDepthwiseConv2D(OriginalDepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop('groups', None)
        super(CustomDepthwiseConv2D, self).__init__(*args, **kwargs)

custom_objects = {'DepthwiseConv2D': CustomDepthwiseConv2D}

# Load models and labels
@st.cache_resource
def load_models():
    models = {}
    labels = {}
    crops = ['tomato', 'potato', 'corn']
    for crop in crops:
        model_path = os.path.join('models', f'{crop}_disease_detection.h5')
        label_path = os.path.join('models', f'{crop}_disease_labels.txt')
        models[crop] = load_model(model_path, custom_objects=custom_objects)
        with open(label_path, 'r') as f:
            labels[crop] = json.load(f)
    return models, labels

models, class_indices = load_models()

# Preprocess image
def preprocess_image(image, target_size=(224, 224)):
    img = image.convert('RGB')
    img = img.resize(target_size)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Predict disease
def predict_disease(crop, image):
    model = models[crop]
    labels = class_indices[crop]
    image_array = preprocess_image(image)
    preds = model.predict(image_array)
    predicted_index = int(np.argmax(preds))
    confidence = float(preds[0][predicted_index])
    disease = list(labels.keys())[list(labels.values()).index(predicted_index)]
    return disease, confidence

# Treatment tips dictionaries
tips = {
    # Add your disease-treatment mappings here
}

generic_tips = {
    'organic': ["Use organic compost."],
    'prevention': ["Regularly inspect plants for early signs of stress or disease. Ensure proper watering, fertilization, and pruning."],
    'rotation': ["Rotate crops annually to maintain soil health."]
}

def get_tips(crop, disease, lang):
    disease_tips = tips.get(crop, {}).get(disease, None)
    if disease_tips:
        organic = disease_tips.get('organic', generic_tips['organic'])
        rotation = disease_tips.get('rotation', generic_tips['rotation'])
        prevention = disease_tips.get('prevention', generic_tips['prevention'])
    else:
        organic = generic_tips['organic']
        rotation = generic_tips['rotation']
        prevention = generic_tips['prevention']

    if lang != 'English':
        try:
            organic = [translator.translate(text, dest=lang).text for text in organic]
            rotation = [translator.translate(text, dest=lang).text for text in rotation]
            prevention = [translator.translate(text, dest=lang).text for text in prevention]
        except Exception as e:
            st.error(f"Translation error: {e}")

    return organic, rotation, prevention

# Language selection
st.markdown('<div class="section-title">🌐 Select Language</div>', unsafe_allow_html=True)
lang = st.selectbox("", options=['English', 'Hindi', 'Marathi', 'Gujarati'], index=0)

# Crop selection
st.markdown('<div class="section-title">🌾 Select Crop</div>', unsafe_allow_html=True)
crop = st.selectbox("", options=['tomato', 'potato', 'corn'])

# Upload file
st.markdown('<div class="section-title">📤 Upload Image</div>', unsafe_allow_html=True)
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_file = st.file_uploader(f"Upload an image of {crop} leaf", type=['jpg', 'jpeg', 'png'])
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file is not None:
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    disease, confidence = predict_disease(crop, image)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🩺 Prediction Results</div>', unsafe_allow_html=True)
    st.markdown(f'<p class="prediction">Disease: {disease}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="confidence">Confidence: {confidence*100:.2f}%</p>', unsafe_allow_html=True)

    organic, rotation, prevention = get_tips(crop, disease, lang)

    st.markdown('<div class="section-title">💡 Treatment Tips</div>', unsafe_allow_html=True)

    st.markdown("**🌿 Organic Remedies:**")
    for tip in organic:
        st.write(f"- {tip}")

    st.markdown("**🔄 Crop Rotation:**")
    for tip in rotation:
        st.write(f"- {tip}")

    st.markdown("**🛡️ Preventive Measures:**")
    for tip in prevention:
        st.write(f"- {tip}")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">© 2025 PlantGuard AI | Made with ❤️ in India</div>', unsafe_allow_html=True)
