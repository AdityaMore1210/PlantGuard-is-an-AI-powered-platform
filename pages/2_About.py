import streamlit as st

# Set page config
st.set_page_config(page_title="About PlantGuard", page_icon="🌿", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 40px;
            color: #2E7D32;
            margin-bottom: 20px;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #555;
            margin-bottom: 30px;
        }
        .features {
            background-color: #E8F5E9;
            padding: 20px;
            border-radius: 15px;
            margin-top: 20px;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #999;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">ℹ️ About <span style="color:#43A047;">PlantGuard</span></div>', unsafe_allow_html=True)

# Subtitle
st.markdown('<div class="subtitle">Your AI-Powered Plant Health Companion 🌿</div>', unsafe_allow_html=True)

# Description
st.write("""
**PlantGuard** is an AI-powered platform designed to help farmers, gardeners, and agriculturalists detect plant diseases early and take timely action.

Simply upload a photo of your plant’s leaf 🍃 — and let our AI model identify the problem while providing tailored, multilingual prevention and treatment advice.
""")

# Features section
st.markdown('<div class="features">', unsafe_allow_html=True)
st.markdown("""
### 🌟 Key Features:
- 📷 **AI-Powered Disease Detection**  
- 📝 **Multilingual Prevention & Treatment Tips**  
- 🌍 **Supports Major Crops:** *Tomato, Potato, and Corn*  
- 💚 **User-Friendly, Intuitive Web Interface**
""")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Built with ❤️ using Streamlit</div>', unsafe_allow_html=True)
