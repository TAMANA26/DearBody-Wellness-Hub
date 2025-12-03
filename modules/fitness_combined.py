import streamlit as st
import pandas as pd

def show_fitness():
    st.markdown("""
        <style>
        .main {
            background: linear-gradient(to right, #ffdde1, #ee9ca7);
            font-family: 'Segoe UI', sans-serif;
            color: #000;
        }
        .stRadio > div {
            flex-direction: row;
            justify-content: center;
        }
        .stSlider > div {
            color: #333;
        }
        .stCheckbox > div {
            margin-bottom: 10px;
        }
        .stTabs [role="tablist"] {
            justify-content: center;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🌈 Welcome to Your DearBody Fitness Hub")

    # Tabs for two sections
    tab1, tab2 = st.tabs(["🏋️ Fitness Tracker", "📚 Fitness Access"])

    # ---------------------- TAB 1: FITNESS TRACKER ---------------------- #
    with tab1:
        st.header("📊 Daily Fitness Tracker")
        
        col1, col2 = st.columns(2)

        with col1:
            water = st.slider("💧 Water Intake (glasses)", 0, 15, 8)
            steps = st.slider("👣 Steps Walked", 0, 20000, 5000, step=1000)
            sleep = st.slider("😴 Sleep Hours", 0, 12, 7)

        with col2:
            workout_done = st.checkbox("🏋️ Completed Workout")
            meditation_done = st.checkbox("🧘 Did Meditation")
            dance_done = st.checkbox("💃 Did Dance")

        st.subheader("📝 Your Daily Summary")
        st.markdown(f"""
            - 💧 **Water Intake:** {water} glasses  
            - 👣 **Steps Walked:** {steps}  
            - 😴 **Sleep Hours:** {sleep}  
            - 🏋️ **Workout:** {'✅' if workout_done else '❌'}  
            - 🧘 **Meditation:** {'✅' if meditation_done else '❌'}  
            - 💃 **Dance:** {'✅' if dance_done else '❌'}
        """)

    # ---------------------- TAB 2: FITNESS ACCESS ---------------------- #
    with tab2:
        st.header("💪 Explore Exercise Library")

        exercises = pd.DataFrame({
            "Exercise": ["Jumping Jacks", "Push-Ups", "Squats", "Plank", "Yoga"],
            "Calories Burned (per 10 mins)": [100, 80, 90, 60, 40],
            "Video": [
                "https://www.youtube.com/watch?v=c4DAnQ6DtF8",
                "https://www.youtube.com/watch?v=_l3ySVKYVJ8",
                "https://www.youtube.com/watch?v=aclHkVaku9U",
                "https://www.youtube.com/watch?v=pSHjTRCQxIw",
                "https://www.youtube.com/watch?v=v7AYKMP6rOE"
            ]
        })

        for i in range(len(exercises)):
            with st.container():
                st.subheader(f"🔥 {exercises['Exercise'][i]}")
                st.write(f"**Calories Burned:** {exercises['Calories Burned (per 10 mins)'][i]} kcal")
                st.video(exercises['Video'][i])
