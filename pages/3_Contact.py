import streamlit as st

# Set page config
st.set_page_config(page_title="Contact PlantGuard", page_icon="📞", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 40px;
            color: #2E7D32;
            margin-bottom: 20px;
        }
        .contact-card {
            background-color: #E8F5E9;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            margin-top: 30px;
            font-size: 20px;
        }
        .contact-item {
            margin: 15px 0;
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
st.markdown('<div class="title">📞 Contact <span style="color:#43A047;">PlantGuard</span></div>', unsafe_allow_html=True)

# Contact card section
st.markdown('<div class="contact-card">', unsafe_allow_html=True)
st.markdown("""
<div class="contact-item">📧 <strong>Email:</strong> <a href="mailto:contact@plantguard.com">contact@plantguard.com</a></div>
<div class="contact-item">📱 <strong>Phone:</strong> +91 9307558946</div>
<div class="contact-item">🌐 <strong>Website:</strong> <a href="https://www.plantguard@gmail.com" target="_blank">www.plantguard.ai</a></div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">We’d love to hear from you! 🌱</div>', unsafe_allow_html=True)
