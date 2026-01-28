import streamlit as st

st.title("Hello Streamlit")
name = st.text_input("Enter your name:")

if st.button("Submit"):
    st.success(f"Welcome {name} ")