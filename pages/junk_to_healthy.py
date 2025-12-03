import streamlit as st

st.markdown(
    """
    <style>
    .main {
        background-color: #fff;
    }
    .stApp {
        background-image: linear-gradient(to right, yellow, #de1f9f, #1fdeb2);
        background-attachment: fixed;
        color: white;
    }
    h2 {
        color: #FFD700;
        text-shadow: 2px 2px 4px #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h2>🍔 Junk to Healthy Alternatives 🥗</h2>", unsafe_allow_html=True)
st.write("Enter a junk food item and we’ll suggest a healthy replacement!")

# Input from user
junk_food = st.text_input("Enter Junk Food (e.g., Pizza, Chips, Soda)")

# Healthy alternatives dictionary
alternatives = {
    "pizza": "Homemade veggie oats chilla with paneer",
    "burger": "Whole wheat sandwich with grilled tofu or veggies",
    "chips": "Roasted chickpeas or baked makhana",
    "soda": "Fresh coconut water or homemade lemon water",
    "chocolate": "Dark chocolate (70%+) or dates with peanut butter",
    "ice cream": "Frozen banana blended with yogurt and berries",
    "maggi": "Homemade vegetable millet noodles"
}

if junk_food:
    lower_input = junk_food.lower()
    if lower_input in alternatives:
        st.markdown(f"""
            <div style="
                background-color: rgba(255, 255, 255, 0.15);
                padding: 15px;
                border-radius: 12px;
                margin-top: 18px;
                font-size: 20px;
                font-weight: bold;
                color: white;
                text-shadow: 1px 1px 3px #f984ef;
                font-family: 'Segoe UI', sans-serif;
                text-align: center;
            ">
                💡 Healthy Alternative for <span style="color: #ffffff;">{junk_food.title()}</span>:<br><br>
                <span style="color: #fff; font-size: 22px; font-weight: bold;">{alternatives[lower_input]}</span>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("😕 Sorry, no suggestion found. Try pizza, burger, chips etc.")
