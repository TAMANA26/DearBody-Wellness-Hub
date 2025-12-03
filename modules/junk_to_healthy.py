# modules/junk_to_healthy.py

import streamlit as st


def junk_to_healthy_section():
    st.markdown("""
        <h2 style='text-align: center; color: #cbffa9;'>🍟➡️🥗 Junk to Healthy Swaps</h2>
        <p style='text-align: center;'>Make smarter choices without sacrificing taste!</p>
    """, unsafe_allow_html=True)

    st.info("Small food swaps can lead to big health results!")

    st.markdown("### 🔁 Common Junk Food Swaps:")

    swaps = [
        {"junk": "Chips", "healthy": "Roasted Chickpeas or Nuts"},
        {"junk": "Sugary Soda", "healthy": "Infused Water or Sparkling Lemon Water"},
        {"junk": "Ice Cream", "healthy": "Frozen Yogurt with Fruit"},
        {"junk": "White Bread", "healthy": "Whole Grain Bread or Multigrain"},
        {"junk": "Chocolate Bar", "healthy": "Dark Chocolate or Dates"},
        {"junk": "Fried Snacks", "healthy": "Air-fried Veggies or Popcorn"},
    ]

    for item in swaps:
        st.markdown(f"🍟 **{item['junk']}** ➡️ 🥦 **{item['healthy']}**")

    st.markdown("### 📸 Inspiration Image:")
    st.image("https://i.imgur.com/5cX1n2T.png", caption="Junk to Healthy Visual", use_column_width=True)

    st.markdown("### 💡 Pro Tip:")
    st.success("Keep healthy snacks visible at home and junk foods out of sight!")

    st.markdown("### 🔍 Why These Swaps?")
    st.markdown("""
    - Reduce sugar & unhealthy fat
    - Improve digestion
    - Maintain steady energy levels
    - Help with weight management
    """)

    st.markdown("<hr>", unsafe_allow_html=True)
