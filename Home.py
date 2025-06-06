import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="🌿 PlantGuard | AI Disease Detector",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide sidebar toggle (hamburger icon)
st.markdown("""
    <style>
    [data-testid="collapsedControl"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# Custom CSS Styling for Homepage
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }

    /* Top Navigation Bar */
    .top-nav {
        display: flex;
        justify-content: center;
        background-color: rgba(0, 0, 0, 0.65);
        padding: 18px;
        border-bottom: 2px solid #43A047;
    }

    .top-nav a {
        color: #ffffff;
        text-decoration: none;
        margin: 0 25px;
        font-size: 20px;
        font-weight: 600;
        padding: 8px 20px;
        border-radius: 8px;
        transition: all 0.3s ease;
    }

    .top-nav a:hover {
        background-color: #43A047;
        color: #fff;
    }

    /* Hero Section */
    .hero-text {
        text-align: center;
        padding-top: 160px;
        padding-bottom: 180px;
        background: rgba(0, 0, 0, 0.55);
        border-radius: 12px;
        margin: 50px 10%;
    }

    .hero-text h1 {
        font-size: 80px;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 25px;
    }

    .hero-text p {
        font-size: 28px;
        color: #dddddd;
        margin-bottom: 20px;
    }

    .hero-text p.sub {
        font-size: 20px;
        color: #cccccc;
        margin-bottom: 40px;
    }

    .stButton>button {
        background-color: #43A047;
        color: white;
        padding: 18px 42px;
        border: none;
        border-radius: 12px;
        font-size: 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        margin-top: 20px;
    }

    .stButton>button:hover {
        background-color: #388E3C;
        transform: scale(1.05);
    }

    /* Footer */
    .footer {
        text-align: center;
        font-size: 14px;
        color: #000000;
        padding: 25px 0;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# Top Navigation Bar
st.markdown("""
<div class="top-nav">
    <a href="/">🏠 Home</a>
    <a href="/Detection">🌿 Detect</a>
    <a href="/About">📖 About</a>
    <a href="/Contact">📞 Contact</a>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-text">
    <h1>🌿 PlantGuard</h1>
    <p>AI-powered Plant Disease Detection & Treatment Guide</p>
    <p class="sub">Protect your crops, boost your harvest, and keep your plants healthy — effortlessly.</p>
</div>
""", unsafe_allow_html=True)

# Start Detection Button Centered
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
if st.button("🚀 Start Detection Now"):
    st.switch_page("pages/1_Detection.py")
st.markdown("</div>", unsafe_allow_html=True)

# Footer Section
st.markdown("""
<div class="footer">
    © 2025 PlantGuard AI | Made with 🌱 for farmers and growers.
</div>
""", unsafe_allow_html=True)
