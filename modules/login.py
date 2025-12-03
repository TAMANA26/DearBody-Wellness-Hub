import streamlit as st

def login_page():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.markdown("<h2 style='text-align: center; color: #FF69B4;'>👋 Welcome to DearBody</h2>", unsafe_allow_html=True)
        name = st.text_input("Enter your name")
        age = st.text_input("Enter your age (optional)")

        if st.button("Login"):
            if name.strip() != "":
                st.session_state.name = name
                st.session_state.logged_in = True
                st.success(f"Welcome, {name}! 🌈 Let's start your journey.")
            else:
                st.warning("Please enter your name to continue.")
    else:
        st.success(f"Welcome, {st.session_state.name}! 🌟")
