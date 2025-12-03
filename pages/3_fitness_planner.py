import streamlit as st
import datetime

# --- Configuration and Setup ---
st.set_page_config(layout="wide")

st.title("🏃 Fitness Planner & Daily Tracker")
st.markdown("Monitor your daily wellness goals here. Input your progress to see if you met your targets!")

# --- 1. Input Section ---
st.header("Daily Input")

# Ensure 'glasses' is defined before being used in the comparison logic.
# We will use st.session_state to make sure the value persists across reruns.

if 'glasses' not in st.session_state:
    st.session_state['glasses'] = 0

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hydration & Sleep")
    # This widget defines and updates the 'glasses' variable in session state
    st.session_state['glasses'] = st.number_input(
        "💧 Glasses of Water Consumed (Target: 8+)",
        min_value=0,
        max_value=20,
        value=st.session_state['glasses'],
        step=1,
        key='water_input'
    )
    sleep_hours = st.slider(
        "😴 Hours of Sleep (Target: 7+)",
        min_value=0.0,
        max_value=12.0,
        value=8.0,
        step=0.5,
        key='sleep_input'
    )

with col2:
    st.subheader("Activity")
    # Define other variables needed for goal tracking
    exercised = st.checkbox("💪 Completed 30+ minutes of Exercise", value=True)
    ate_vegetables = st.checkbox("🥗 Ate at least 3 servings of Vegetables", value=True)
    meditated = st.checkbox("🧘 Completed 10 minutes of Meditation", value=False)
    
# Get the defined value from session state for the goal comparison logic
# The variable 'glasses' is now correctly defined.
glasses = st.session_state['glasses']


# --- 2. Goal Tracking Logic (This is where the original error occurred) ---
st.header("Goal Progress")
st.subheader(f"Tracker for {datetime.date.today().strftime('%A, %B %d, %Y')}")

# A list of tuples: (Goal Description, Goal Met Condition)
daily_goals = [
    # FIX: 'glasses' is now defined above via st.session_state
    ("💧 Water", glasses >= 8), 
    ("😴 Sleep", sleep_hours >= 7),
    ("💪 Exercise", exercised),
    ("🥗 Nutrition", ate_vegetables),
    ("🧘 Mindfulness", meditated)
]

# --- 3. Display Results ---
total_goals = len(daily_goals)
goals_met = sum(1 for _, met in daily_goals if met)
progress_percentage = (goals_met / total_goals) * 100 if total_goals > 0 else 0

st.metric(label="Total Goals Met", value=f"{goals_met} / {total_goals}", delta=f"{progress_percentage:.0f}% Progress")

st.markdown("---")

for description, met in daily_goals:
    if met:
        st.success(f"✅ {description}: Goal Met!")
    else:
        st.warning(f"❌ {description}: Needs Improvement.")


# --- Additional Suggestions ---
st.markdown("""
<style>
    .stNumberInput, .stSlider {
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.caption("This is a simplified planner. You can expand it with Firestore for persistent tracking!")
