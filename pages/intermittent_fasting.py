import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Fasting Guide", layout="wide")

# 💄 UI Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffe6e6, #f9f5f5);
}
h2 {
    color: #d63384;
    text-align: center;
    text-shadow: 1px 1px 2px #aaa;
}
.card {
    background-color: #fff0f5;
    padding: 1.5rem;
    border-radius: 15px;
    box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# 🏷️ Title
st.markdown("<h2>⏳ Intermittent Fasting Planner</h2>", unsafe_allow_html=True)

# 🔁 Choose Fasting Type
fasting_type = st.selectbox("Choose your fasting method", ["16:8", "18:6", "20:4", "OMAD (One Meal A Day)"])

# ✍️ Fasting Tip Box
st.markdown(f"""
<div class="card">
    <h4 style='color:#cc3366;'>How {fasting_type} Works:</h4>
    <p>
        - You fast for <b>{fasting_type.split(':')[0]}</b> hours and eat during <b>{fasting_type.split(':')[1]}</b> hours.<br>
        - Helps improve insulin sensitivity and boosts fat burning.<br>
        - Drink water, black coffee, or green tea during fasting.
    </p>
</div>
""", unsafe_allow_html=True)

# 🍱 Sample Meal Plan
st.markdown("""
<div class="card">
    <h4 style='color:#cc3366;'>🍽️ Sample Healthy Meal Ideas</h4>
    <ul>
        <li>Oats with banana and nuts</li>
        <li>Grilled paneer salad with veggies</li>
        <li>Lentil soup with brown rice</li>
        <li>Coconut water and fruits</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# 📊 Visualization
st.markdown("### 🧪 Your Fasting Window:")
hours = [int(fasting_type.split(":")[0]), int(fasting_type.split(":")[1])]
labels = ['Fasting', 'Eating']
colors = ['#ffb6c1', '#d8bfd8']

fig, ax = plt.subplots()
ax.pie(hours, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)
