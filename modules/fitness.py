import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import webbrowser


st.set_page_config(page_title="Fitness Planner", layout="wide")

# ----------------- HEADER ------------------
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🏋️‍♀️ DearBody Fitness Planner 💪</h1>", unsafe_allow_html=True)
st.markdown("### Start strong. Stay consistent. Finish proud! 🔥")

# ----------------- BMI CALCULATOR ------------------
with st.expander("📏 Click to Calculate Your BMI"):
    height = st.number_input("📐 Enter your height in cm:", min_value=100, max_value=250, value=165)
    weight = st.number_input("⚖️ Enter your weight in kg:", min_value=20, max_value=200, value=60)

    if height and weight:
        bmi = weight / ((height / 100) ** 2)
        st.success(f"🎯 Your BMI is: **{bmi:.2f}**")

        if bmi < 18.5:
            status = "Underweight"
            emoji = "😟"
            color = "orange"
            tip = "Eat more protein & healthy carbs."
        elif 18.5 <= bmi < 25:
            status = "Normal"
            emoji = "😄"
            color = "green"
            tip = "You're doing great! Maintain this."
        elif 25 <= bmi < 30:
            status = "Overweight"
            emoji = "😐"
            color = "gold"
            tip = "Try daily walking & reduce sugar intake."
        else:
            status = "Obese"
            emoji = "😓"
            color = "red"
            tip = "Consult a doctor & follow an active routine."

        st.markdown(f"**Status**: <span style='color:{color}'><strong>{status} {emoji}</strong></span>", unsafe_allow_html=True)
        st.info(f"💡 Health Tip: {tip}")

# ----------------- SIDEBAR GOAL SELECT ------------------
goal = st.selectbox("🎯 Choose Your Fitness Goal", ["Weight Loss", "Muscle Gain", "Stay Active"])

# ----------------- EXERCISES & CALORIES ------------------
exercise_plan = {
    "Weight Loss": {
        "exercises": ["Jumping Jacks", "Mountain Climbers", "Running", "Cycling"],
        "calories": [200, 250, 300, 150],
        "intensity": [7, 8, 9, 6]
    },
    "Muscle Gain": {
        "exercises": ["Pushups", "Squats", "Deadlifts", "Bench Press"],
        "calories": [120, 200, 250, 220],
        "intensity": [6, 9, 9, 8]
    },
    "Stay Active": {
        "exercises": ["Walking", "Yoga", "Stretching", "Dancing"],
        "calories": [80, 90, 50, 120],
        "intensity": [4, 5, 3, 6]
    }
}

exercises = exercise_plan[goal]["exercises"]
calories = exercise_plan[goal]["calories"]
intensity = exercise_plan[goal]["intensity"]

# ----------------- LAYOUT ------------------
col1, col2 = st.columns([1, 2])

# --------- COLUMN 1: Today’s Workout Plan ----------
with col1:

    st.subheader("📅 Today's Workout Plan")
    st.markdown(f"Here's your customized workout for **{goal}**:")
    for i, ex in enumerate(exercises):
        st.markdown(f"**{i+1}. {ex}**")
    st.success("✅ You're all set for the day! Keep pushing forward!")
    st.markdown("---")

    import streamlit as st

# --- Initialize States ---
if 'water_drank' not in st.session_state:
    st.session_state.water_drank = 0
if 'daily_goal' not in st.session_state:
    st.session_state.daily_goal = 2000  # Default: 2L

st.markdown("## 💧 Smart Water Tracker")

# --- USER SET DAILY GOAL ---
goal = st.number_input("Set your water goal for the day (ml):", 1000, 5000, 2000, step=100)
st.session_state.daily_goal = goal

# --- USER INPUT HOW MUCH THEY DRANK NOW ---
new_input = st.number_input("Tell me how much water of the day you drank till now (ml):", 0, 2000, step=50)

if st.button("📥 Submit"):
    st.session_state.water_drank += new_input
    st.success(f"Recorded: {new_input}ml added to your tracker!")

# --- Calculate Progress ---
drank = st.session_state.water_drank
goal = st.session_state.daily_goal
percent = int((drank / goal) * 100)
if percent > 100:
    percent = 100

remaining = goal - drank if drank < goal else 0

# --- Suggestion Message ---
if percent >= 100:
    message = "🎉 You've met your goal! Stay hydrated!"
elif percent >= 75:
    message = "💪 Almost there! Keep it up!"
elif percent >= 50:
    message = "🙂 You're halfway done! Drink a little more."
elif percent >= 25:
    message = "🚰 You need more water to stay active!"
else:
    message = "😟 You're far behind! Drink up for your health!"

st.markdown(f"### 🧠 Suggestion: {message}")
st.markdown(f"**You have consumed:** {drank}ml / {goal}ml")
st.markdown(f"**Remaining:** {remaining}ml")

# --- 3D Animated Water Glass ---
glass_html = f"""
<style>
.glass {{
    width: 120px;
    height: 250px;
    border: 4px solid #00bcd4;
    border-radius: 15px;
    position: relative;
    margin: auto;
    background: #e0f7fa;
    overflow: hidden;
    box-shadow: inset 0 0 25px rgba(0,188,212,0.4);
}}

.water {{
    position: absolute;
    bottom: 0;
    width: 100%;
    height: {percent}%;
    background: linear-gradient(to top, #00bcd4, #4dd0e1);
    animation: wave 2s ease-in-out infinite;
}}

@keyframes wave {{
    0% {{ transform: translateY(0); }}
    50% {{ transform: translateY(-4px); }}
    100% {{ transform: translateY(0); }}
}}

.text {{
    text-align: center;
    font-size: 16px;
    color: #00796b;
    font-weight: bold;
    margin-top: 10px;
}}
</style>

<div class="glass">
    <div class="water"></div>
</div>
<div class="text">💦 {percent}% of {goal}ml</div>
"""

st.markdown(glass_html, unsafe_allow_html=True)

# --------- COLUMN 2: Tabs with Charts ----------
with col2:
    tab1, tab2, tab3 = st.tabs(["🔥 Calories Burn", "📉 Progress Tracker", "📍 Effort vs Burn"])
    

    # Tab 1: Calories Burn Chart


# Inside tab1:
with tab1:
        fig1, ax1 = plt.subplots()
        ax1.bar(exercises, calories, color='mediumseagreen')
        ax1.set_ylabel("Calories Burned")
        ax1.set_title("Calories Burned per Exercise")
        st.pyplot(fig1)
        st.markdown("---")
with tab1:
    st.markdown("## 💬 Daily Motivation")

    # List of motivational quotes
    quotes = [
        "🏋️‍♀️ Push yourself because no one else is going to do it for you.",
        "🔥 Don’t stop when you’re tired, stop when you’re done.",
        "🚀 One workout at a time. One day at a time.",
        "🌟 Strive for progress, not perfection.",
        "🧠 Your body can stand almost anything. It’s your mind that you have to convince.",
        "💡 Little by little, a little becomes a lot.",
    ]

    # Pick a random quote
    st.success(random.choice(quotes))
    st.markdown("---") 

    # Workout Music Button
    st.markdown("### 🎵 Need a boost? Hit the workout playlist!")
    if st.button("▶️ Play Workout Music"):
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=2z8JmcrW-As")  # Replace with any energetic playlist
    st.markdown("---") 
with tab1:
    st.markdown("## 📆 Emoji Habit Tracker - How Was Your Day?")

    col1, col2, col3 = st.columns(3)

    with col1:
        water = st.checkbox("💧 Drank enough water?")
        steps = st.checkbox("🚶‍♀️ Walked 5K+ steps?")

    with col2:
        sleep = st.checkbox("😴 Slept 7-8 hours?")
        meals = st.checkbox("🍽️ Ate 3 healthy meals?")

    with col3:
        mood = st.checkbox("😊 Felt happy today?")

    # Count total checked
    total_done = sum([water, steps, sleep, meals, mood])


    st.markdown(f"### ✅ You completed `{total_done}/5` habits today!")
    st.progress(total_done / 5)

    # Achievement badge 🎖️
    if total_done == 5:
        st.balloons()
        st.success("🥇 Champion! You're on fire today!")
    elif total_done >= 3:
        st.info("🥈 Active! Keep going strong.")
    elif total_done >= 1:
        st.warning("🥉 Beginner! You started — that's what matters.")
    else:
        st.error("😴 Lazy day? Let's do better tomorrow!")
    st.markdown("---")
    

    # Tab 2: Progress Over Weeks
    with tab2:
        st.markdown("💡 Sample weight tracking over 6 weeks")
        weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6"]
        if goal == "Weight Loss":
            weight = [70, 69, 68, 67.2, 66.5, 65.8]
        elif goal == "Muscle Gain":
            weight = [55, 56, 57.2, 58, 59, 60]
        else:
            weight = [60, 60.1, 60.2, 60.1, 60.0, 60.2]
        fig2, ax2 = plt.subplots()
        ax2.plot(weeks, weight, marker='o', color='tomato')
        ax2.set_ylabel("Weight (kg)")
        ax2.set_title("Weight Progress Over Time")
        st.pyplot(fig2)
        

    

    # Tab 3: Scatter Plot - Intensity vs Calories
    with tab3:
        fig3, ax3 = plt.subplots()
        ax3.scatter(intensity, calories, color='orchid', s=150)

        for i, label in enumerate(exercises):
            ax3.annotate(label, (intensity[i] + 0.05, calories[i] + 5), fontsize=9)

        ax3.set_xlabel("Exercise Intensity (1–10)")
        ax3.set_ylabel("Calories Burned")
        ax3.set_title("📍 Effort vs Burn: Intensity vs Calories")
        st.pyplot(fig3)
        
    

        # ----------------- WEEKLY FITNESS PLANNER ------------------
st.subheader("📆 Weekly Fitness Planner")

weekly_plan = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Focus": [
        "Upper Body Strength", 
        "Cardio + Abs", 
        "Lower Body Blast", 
        "Active Recovery (Yoga)", 
        "HIIT Circuit", 
        "Outdoor Fun (Walk/Dance)", 
        "Rest & Recharge"
    ],
    "Suggested Time": ["45 mins", "40 mins", "50 mins", "30 mins", "45 mins", "60 mins", "0 mins"]
}

weekly_df = pd.DataFrame(weekly_plan)
st.dataframe(weekly_df, use_container_width=True)
st.info("✅ Pro Tip: Stick to this routine for 3–4 weeks and adjust as needed!")



# ----------------- FOOTER ------------------
st.markdown("---")
st.markdown("<center><small>💚 Built with love by DearBody | Keep moving, keep glowing!</small></center>", unsafe_allow_html=True)
