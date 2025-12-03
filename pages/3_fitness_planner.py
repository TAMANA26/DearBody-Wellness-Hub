# app.py
import streamlit as st
import time
import plotly.express as px
from modules.login import login_page
from modules.intermittent_fasting import fasting_section
from modules.junk_to_healthy import junk_to_healthy_section
from modules.csv_tracker import csv_section

# Page Config
st.set_page_config(layout="wide")

# Rainbow Background
st.markdown('<style>' + open('styles/rainbow.css').read() + '</style>', unsafe_allow_html=True)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, 
            #fcb1d1, #f8c3ec, #d6c1ff, #c1d8ff, #b5f3e0, #fff1a8, #ffcda9);
        background-size: 140% 140%;
        animation: gradientMove 20s ease infinite;
    }
    @keyframes gradientMove {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    </style>
""", unsafe_allow_html=True)

# Login Section
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_page()
    st.stop()

# Page Title
st.markdown("""
    <h1 style='text-align: center; color: white;'>🍎 DearBody</h1>
    <h3 style='text-align: center; color: white;'>✨ One Page to Track Your Fitness, Food & Fasting Goals ✨</h3>
""", unsafe_allow_html=True)

# Main Section Navigation
selected_main = st.selectbox("⬇️ Choose a Section to View", [
    '🏋️ Fitness Planner', '🕐 Intermittent Fasting', '🍟 Junk to Healthy', '📊 CSV Tracker'],
    index=0)

# Sub-section for Fitness Planner
if selected_main == '🏋️ Fitness Planner':
    st.markdown("""<h2 style='color:#fff;text-align:center;'>Choose a Fitness Tool</h2>""", unsafe_allow_html=True)
    selected_fitness = st.radio("", ["Fitness Tracker", "Fitness Access"], horizontal=True)

    if selected_fitness == "Fitness Tracker":
        st.header("📊 Daily Fitness Tracker")

        col1, col2 = st.columns(2)
        with col1:
    st.subheader("💧 Water Intake Tracker")
    glasses = st.slider("How many glasses of water did you drink today?", 0, 15, 8)
    
    # Display current status using a progress bar (replaces the image visually)
    target_glasses = 8
    progress_percent = min(100, (glasses / target_glasses) * 100)
    st.progress(progress_percent / 100)
    
    st.markdown(f"**Current Intake:** {glasses} / {target_glasses} glasses")

    if glasses < target_glasses:
        st.warning(f"💧 Try drinking {target_glasses - glasses} more glasses to meet your goal!")
    else:
        st.success("✅ Excellent hydration! Keep it up.")

            st.subheader("🍎 Healthy Food")
            food_done = st.checkbox("Ate Healthy Meals Today?")
            if not food_done:
                st.info("Try including fruits and veggies 🥗")

            st.subheader("🏋️ Exercise")
            exercise_done = st.checkbox("Completed Exercise?")
            if not exercise_done:
                st.info("Even a 10-min walk helps! 🚶‍♀️")

            st.subheader("😴 Sleep Tracker")
            sleep = st.slider("How many hours did you sleep?", 0, 12, 7)
            sleep_done = sleep >= 7
            if not sleep_done:
                st.warning(f"You need around {7 - sleep} more hours of sleep 😴")

            st.subheader("😀 Mood")
            mood = st.radio("How do you feel today?", ["😀", "😐", "😫", "😴", "🤒"], horizontal=True)

        with col2:
            st.subheader("🧠 Motivation")
            quotes = [
                "Push through the pain, it’s worth it 💥",
                "Every drop of sweat counts 💦",
                "Show up, even when it's hard 🙌",
                "Fuel your fire 🔥",
                "You’re stronger than your excuses 💪"
            ]
            st.success(st.selectbox("Today's Motivation", quotes))

            st.subheader("🎧 Relaxing Music")
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

            st.subheader("🎯 Health Emoji Tracker")
            goals = [
                ("💧 Water", glasses >= 8),
                ("🍎 Food", food_done),
                ("🏋️ Exercise", exercise_done),
                ("😴 Sleep", sleep_done),
                ("😀 Mood", mood == "😀")
            ]
            achieved = sum([1 for _, done in goals if done])

            for emoji, done in goals:
                st.markdown(f"{emoji} {'✅' if done else '❌'}")

            if achieved == 5:
                st.balloons()
                st.success("🎉 All 5 Daily Health Goals Achieved! You're unstoppable!")
            else:
                st.info(f"⭐ You completed {achieved}/5 goals. Let's hit 5 tomorrow!")

            if achieved <= 3:
                st.error("💡 Tip: Try setting small hourly reminders for water, food, or breaks!")

        st.markdown("---")
        st.subheader("📆 Weekly Planner (Sample Chart)")
        week_data = {
            "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "Calories Burned": [220, 180, 260, 300, 190, 150, 200]
        }
        fig = px.line(week_data, x="Day", y="Calories Burned", markers=True, title="Calories Burned Over the Week")
        st.plotly_chart(fig)
