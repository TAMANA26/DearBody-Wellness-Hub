import streamlit as st
from datetime import datetime, timedelta

def fitness_section():
    # --- Custom CSS for Fitness Planner ---
    st.markdown("""
    <style>
    /* Main Container */
    .fitness-container {
        padding: 10px;
        border-radius: 10px;
        margin-top: 15px;
        background: rgba(255, 255, 255, 0.7);
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    h2, h3 {
        color: #4a148c;
        text-align: center;
        font-weight: 700;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    /* Date Navigation */
    .date-nav {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
    }
    .date-nav .stButton button {
        background: #f0f2f5;
        border: 1px solid #ddd;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        font-size: 1.2rem;
        color: #4a148c;
        transition: all 0.2s;
    }
    .date-nav .stButton button:hover {
        background: #e0e0e0;
        transform: scale(1.1);
    }
    .date-display {
        font-size: 1.5rem;
        font-weight: bold;
        color: #4a148c;
        margin: 0 20px;
    }
    
    /* Metric Cards and Circular Progress Bars */
    .metric-card {
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        background: #ffffff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-5px);
    }
    .metric-title {
        font-weight: bold;
        color: #6c757d;
        margin-bottom: 15px;
    }
    .circular-progress {
        position: relative;
        width: 100px;
        height: 100px;
        border-radius: 50%;
        display: grid;
        place-items: center;
        margin: auto;
    }
    .circular-progress::before {
        content: "";
        position: absolute;
        height: 84%;
        width: 84%;
        background-color: #ffffff;
        border-radius: 50%;
    }
    .progress-value {
        position: relative;
        font-size: 1.1rem;
        font-weight: bold;
        color: #4a148c;
    }
    
    /* Workout Checklist */
    .workout-card {
        padding: 20px;
        border-radius: 10px;
        background: #ffffff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-top: 20px;
    }
    .workout-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #4a148c;
        margin-bottom: 15px;
        text-align: center;
    }
    .stCheckbox label {
        font-size: 1rem;
        color: #34495e;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="fitness-container">', unsafe_allow_html=True)
    
    st.markdown("<h2>🏋️ Fitness Plan</h2>", unsafe_allow_html=True)

    # Initialize session state for date and fitness data
    if 'current_date' not in st.session_state:
        st.session_state.current_date = datetime.now().date()
    if 'fitness_data' not in st.session_state:
        st.session_state.fitness_data = {}
        
    def get_day_data(date):
        date_str = date.strftime('%Y-%m-%d')
        if date_str not in st.session_state.fitness_data:
            st.session_state.fitness_data[date_str] = {
                'water_intake': 0,
                'water_goal': 2000,
                'calories_burned': 0,
                'calories_goal': 500,
                'workout_completed': {'Push-ups': False, 'Squats': False, 'Plank': False, 'Jogging': False}
            }
        return st.session_state.fitness_data[date_str]

    # --- Date Navigation ---
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("⬅️"):
            st.session_state.current_date -= timedelta(days=1)
    with col2:
        st.markdown(f"<div class='date-display' style='text-align: center;'>{st.session_state.current_date.strftime('%B %d, %Y')}</div>", unsafe_allow_html=True)
    with col3:
        if st.button("➡️"):
            st.session_state.current_date += timedelta(days=1)
            
    # Get today's data or a new day's data
    day_data = get_day_data(st.session_state.current_date)
    
    # --- Goal Metrics Section (Water and Calories) ---
    col_water, col_calories = st.columns(2)
    
    with col_water:
        water_progress = (day_data['water_intake'] / day_data['water_goal']) * 100
        water_progress = min(water_progress, 100) # Cap at 100%
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">WATER INTAKE</div>
            <div class="circular-progress" style="background: conic-gradient(#4e73df {water_progress}%, #f0f2f5 {water_progress}%);">
                <span class="progress-value">{day_data['water_intake']} ml</span>
            </div>
            <p style="margin-top: 10px; font-size: 0.9rem; color: #555;">Goal: {day_data['water_goal']} ml</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Add a way to update water intake
        if st.session_state.current_date == datetime.now().date():
            update_water = st.number_input("Add Water (ml)", min_value=0, step=250, key="water_input", label_visibility="collapsed")
            if st.button("Add"):
                day_data['water_intake'] += update_water
                st.session_state.fitness_data[st.session_state.current_date.strftime('%Y-%m-%d')] = day_data
                st.rerun()

    with col_calories:
        calorie_progress = (day_data['calories_burned'] / day_data['calories_goal']) * 100
        calorie_progress = min(calorie_progress, 100) # Cap at 100%
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">CALORIES BURNED</div>
            <div class="circular-progress" style="background: conic-gradient(#e74c3c {calorie_progress}%, #f0f2f5 {calorie_progress}%);">
                <span class="progress-value">{day_data['calories_burned']} Kcal</span>
            </div>
            <p style="margin-top: 10px; font-size: 0.9rem; color: #555;">Goal: {day_data['calories_goal']} Kcal</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.current_date == datetime.now().date():
            update_calories = st.number_input("Add Calories Burned (Kcal)", min_value=0, step=50, key="calorie_input", label_visibility="collapsed")
            if st.button("Add "):
                day_data['calories_burned'] += update_calories
                st.session_state.fitness_data[st.session_state.current_date.strftime('%Y-%m-%d')] = day_data
                st.rerun()

    # --- Today's Workout Checklist ---
    st.markdown('<div class="workout-card">', unsafe_allow_html=True)
    st.markdown("<h3 class='workout-title'>💪 Today's Workout</h3>", unsafe_allow_html=True)
    
    workout_plan = day_data['workout_completed']
    
    for exercise, is_completed in workout_plan.items():
        # Check if the workout is for today to allow changes
        if st.session_state.current_date == datetime.now().date():
            checked = st.checkbox(exercise, value=is_completed, key=f"workout_{exercise}_{st.session_state.current_date}")
            workout_plan[exercise] = checked
        else:
            # Display a disabled checkbox for past/future days
            if is_completed:
                st.markdown(f"<p style='color: green;'>✅ {exercise}</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p style='color: grey;'>☐ {exercise}</p>", unsafe_allow_html=True)

    # Save changes to session state if it's the current date
    if st.session_state.current_date == datetime.now().date():
        st.session_state.fitness_data[st.session_state.current_date.strftime('%Y-%m-%d')] = day_data
        
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)