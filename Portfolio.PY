import streamlit as st
import os
from pathlib import Path

# Page config
st.set_page_config(page_title="PyExpo Portfolio", page_icon="🌟")

# Sidebar (navigation + persistent image)
st.sidebar.title("Location")
menu = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Contact"])

# Show a persistent profile image in the sidebar so it stays visible across pages.
ASSETS_DIR = Path(__file__).parent / "assets"
PROFILE_PATH = ASSETS_DIR / "profile.png"

if PROFILE_PATH.exists():
    st.sidebar.image(str(PROFILE_PATH), use_column_width=True)
else:
    # Placeholder image shown when local image is missing
    st.sidebar.image(
        "https://via.placeholder.com/250x250.png?text=Profile+Image",
        use_column_width=True,
    )
    st.sidebar.markdown("Place your image at `assets/profile.png` to replace the placeholder")

# Home
if menu == "Home":
    st.title("👩‍💻PyExpo")
    st.subheader("Aspiring Full Stack Developer")
    st.write("Welcome to my Streamlit portfolio!")

# About
elif menu == "About":
    st.header("📌 About Me")
    st.write("""
    - Newbie Full Stack Developer""")

# Projects
elif menu == "Projects":
    st.header("🛠 Projects")
    st.write("🔹 Student Feedback System")
    st.write("🔹 Travel Content App")
    st.write("🔹 GitHub Portfolio Website")

# Contact
elif menu == "Contact":
    st.header("📞 Contact Me")
    email = st.text_input("Enter your email")
    msg = st.text_area("Your message")

    if st.button("Send"):
        st.success("Message sent successfully ✅")
