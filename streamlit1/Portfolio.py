import streamlit as st
import os
from pathlib import Path

# Page config
st.set_page_config(page_title="PyExpo Portfolio", page_icon="🌟")

# Sidebar (navigation + persistent image)
st.sidebar.title("Location")
menu = st.sidebar.radio("Go to", ["Dashboard", "Who I Am", "Builds", "Reach out"])

# Show a persistent profile image in the sidebar so it stays visible across pages.
ASSETS_DIR = Path(__file__).parent / "assets"
PROFILE_PATH = ASSETS_DIR / "pic.jpg"

if PROFILE_PATH.exists():
    st.sidebar.image(str(PROFILE_PATH), width=250)
else:
    # Placeholder image shown when local image is missing
    st.sidebar.image(
        "https://via.placeholder.com/250x250.png?text=Profile+Image",
        width=250,
    )
    st.sidebar.markdown("Place your image at `assets/pic.jpg` to replace the placeholder")

# Home
if menu == "Dashboard":
    st.title("👩‍💻PyExpo")
    st.subheader("Future Full Stack Developer")
    st.write("Welcome to my PyExpo Streamlit portfolio!")
    
    # Display the image in the dashboard
    if PROFILE_PATH.exists():
        st.image(str(PROFILE_PATH), width=400)
    else:
        st.image(
            "https://via.placeholder.com/400x400.png?text=codeeee pic.jng",
            width=400,
        )

# About
elif menu == "Who I Am":
    st.header("📌 About Me")
    st.write("""
    - Newbie 
    - Enthusiastic
    - Programming Explorer
    - Creative learner""")

# Projects
elif menu == "Builds":
    st.header("🛠 Builds")
    st.write("🔹 Student Feedback System")
    st.write("🔹 Bank Management System")
    st.write("🔹 Student attendance System")

# Contact
elif menu == "Reach out":
    st.header("📞 Contact Me")
    email = st.text_input("Enter your correct email")
    msg = st.text_area("Your valuable message")

    if st.button("Send"):
        st.success("Message sent successfully ✅, I will get back to you soon!")