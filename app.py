import webbrowser
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from modules.intermittent_fasting import fasting_section
import random

# Page config
st.set_page_config(layout="wide")
st.markdown('<style>' + open('styles/rainbow.css').read() + '</style>', unsafe_allow_html=True)

# Custom CSS for the BMI calculator and other sections
st.markdown("""
    <style>
    /* Styling for the BMI calculator container */
    .bmi-container {
        background-color: rgba(255, 255, 255, 0.6);
        border-radius: 03px;
        padding: 05px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin: 25px 0;
    }
    
    .calorie-container {
        background-color: rgba(255, 255, 255, 0.6);
        border-radius: 00px;
        padding: 00px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin: 25px 0;
    }
    
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

# Title
st.markdown("<h1 style='text-align: center; color: white;'> DearBody</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>✨ One Page to Track Your Fitness, Food & Fasting Goals ✨</h3>", unsafe_allow_html=True)

# --- JUNK TO HEALTHY SECTION (NEW & IMPROVED) ---
def junk_section():
    st.markdown("""
    <style>
    /* Styling for the whole junk section to give it a different background */
    .junk-section-container {
        padding: 30px;
        border-radius: 20px;
        margin: 20px 0;
    }

    /* Styling for the search result pop-out */
    .swap-result-box {
        background-color: rgba(255, 255, 255, 0.9);
        border-left: 5px solid #20c997;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        animation: slideIn 0.5s ease-out;
    }
    @keyframes slideIn {
        from { transform: translateY(-20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    /* Styling for the unique swapping cards */
    .swap-card {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
        transition: transform 0.2s;
    }
    .swap-card:hover {
        transform: translateY(-5px);
    }
    .swap-arrow {
        color: #ff5e62;
        font-size: 24px;
        font-weight: bold;
        animation: bounce 1.5s infinite;
    }
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="junk-section-container">', unsafe_allow_html=True)
    st.markdown("""
        <h2 style='text-align: center; color: #6a11cb;'>🍟➡️🥗 Junk to Healthy Swaps</h2>
        <p style='text-align: center; color: #4a4a4a;'>Make smarter choices without sacrificing taste!</p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True) # Add some space

    # Interactive input section with a dropdown
    st.markdown("### 🔍 Find a Healthy Swap")
    
    swaps_dict = {
        "Chips": "Baked kale chips or roasted chickpeas",
        "Soda": "Sparkling water with a lemon slice",
        "Ice Cream": "Frozen banana 'nice' cream",
        "White Bread": "Whole-grain bread or lettuce wraps",
        "Chocolate Bar": "A square of dark chocolate (70% or more)",
        "Fried Snacks": "Air-fried vegetables or unbuttered popcorn",
        "Pizza": "Homemade pizza with a cauliflower crust and lots of veggies",
        "Burgers": "A homemade burger with a lean patty on a whole-wheat bun",
        "French Fries": "Baked sweet potato fries",
        "Candy": "Fresh fruit like grapes or an apple",
        "Cookies": "Oatmeal cookies with raisins",
        "Cereal": "Oatmeal with berries",
        "Doughnut": "Greek yogurt with honey and nuts",
        "Cake": "Angel food cake with fresh strawberries",
        "Potato Chips": "Air-popped popcorn with a pinch of sea salt",
        "White Rice": "Quinoa or brown rice",
        "Sugary Drinks": "Herbal tea or infused water",
        "Instant Noodles": "Whole-wheat pasta or chickpea noodles",
        "Processed Meat": "Lean chicken or fish"
    }

    junk_food_selected = st.selectbox(
        "Choose a junk food to find a healthy alternative:",
        options=[""] + list(swaps_dict.keys()),
        index=0,
        help="Select a food to see a healthy swap."
    )
    
    if junk_food_selected:
        found_swap = swaps_dict.get(junk_food_selected, None)
        if found_swap:
            st.markdown(f"""
            <div class="swap-result-box">
                <p><strong>Instead of <span style="color:#ff5e62;">{junk_food_selected}</span>, try:</strong></p>
                <p style="font-size: 18px; color:#20c997; font-weight: bold;">{found_swap}!</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)

    # Static list of swaps with a creative card design
    st.markdown("### 📋 Our Top Swaps List")
    st.markdown("<p style='color: #4a4a4a;'>Here are some of the most popular swaps you can make today!</p>", unsafe_allow_html=True)
    
    swaps = [
        {"junk_icon": " chips", "junk": "Chips", "healthy_icon": " nuts", "healthy": "Roasted Chickpeas or Nuts", "tip": "Why? They are rich in protein and healthy fats, keeping you full longer and providing sustained energy. A great source of fiber!"},
        {"junk_icon": " pizza", "junk": "Pizza", "healthy_icon": " salad", "healthy": "Cauliflower Crust Pizza", "tip": "Why? It significantly cuts down on carbs and calories while adding a serving of vegetables. Top with fresh veggies for extra vitamins and fiber!"},
        {"junk_icon": " soda", "junk": "Sugary Soda", "healthy_icon": " water", "healthy": "Infused Water", "tip": "Why? Eliminates empty calories and sugar spikes, while keeping you hydrated. Add cucumber or mint for flavor and a hint of freshness."},
        {"junk_icon": " bread", "junk": "White Bread", "healthy_icon": " bread", "healthy": "Whole Grain Bread", "tip": "Why? Higher in fiber and nutrients, promoting better digestion and providing more energy throughout the day. It helps maintain stable blood sugar levels."},
        {"junk_icon": " ice_cream", "junk": "Ice Cream", "healthy_icon": " yogurt", "healthy": "Frozen Banana 'Nice' Cream", "tip": "Why? Lower in sugar and saturated fat, plus you get the benefits of natural fruit sweetness. A guilt-free, creamy treat!"},
        {"junk_icon": " coffee", "junk": "Sweet Coffee", "healthy_icon": " tea", "healthy": "Black Coffee with Cinnamon", "tip": "Why? Ditch the syrups and sugar to cut down on calories. Cinnamon adds natural sweetness and has powerful antioxidant properties."},
    ]

    for item in swaps:
        st.markdown('<div class="swap-card">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 4])
        with col1:
            st.markdown(f"**:{item['junk_icon']}:**")
        with col2:
            st.markdown(f'<span class="swap-arrow">➡️</span>', unsafe_allow_html=True)
        with col3:
            st.markdown(f"**{item['junk']}** ➡️ **{item['healthy']}**")
            with st.expander("💡 Why it's a better choice?"):
                st.write(item['tip'])
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### 🌟 Daily Motivation")
    
    motivation_tips = [
        "Keep healthy snacks visible at home and junk foods out of sight!",
        "Meal prep your healthy snacks for the week to avoid last-minute cravings.",
        "When a craving hits, drink a glass of water first. Sometimes you're just thirsty!",
        "Try new spices and herbs on your food to boost flavor without adding salt or sugar.",
        "An air fryer is your best friend for making crispy, healthy versions of your favorite fried foods."
    ]

    if st.button("✨ Get a Random Tip"):
        st.info(random.choice(motivation_tips))

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Dropdown Navigation
selected = st.selectbox("⬇️ Choose a Section to View", 
                            ['🏋️ Fitness Planner', '🕐 Intermittent Fasting', '📊 CSV Tracker', '🍟 Junk to Healthy'],
                            index=0)

# FITNESS PLANNER SECTION
if selected == '🏋️ Fitness Planner':
    st.markdown("### 🔥 Your Workout Plan")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🕺 Jumping Jacks")
        st.info("Duration: 10 mins\nCalories: 100 kcal")
        st.link_button("▶️ Watch Video", "https://www.youtube.com/watch?v=c4DAnQ6DtF8")
    
    with col2:
        st.markdown("#### 🏋️ Squats")
        st.info("Duration: 20 mins\nCalories: 100 kcal")
        st.link_button("▶️ Watch Video", "https://www.youtube.com/watch?v=aclHkVaku9U")
    
    with col3:
        st.markdown("#### 🧗 Mountain Climbers")
        st.info("Duration: 10 mins\nCalories: 120 kcal")
        st.link_button("▶️ Watch Video", "https://www.youtube.com/watch?v=nmwgirgXLYM")
    
    st.markdown("---")
    
    # ----------------- DYNAMIC CALORIE ESTIMATOR (NEW & IMPROVED) ------------------
    st.markdown("## ✨ Personalized Calorie Burn Estimator")
    with st.container(border=False):
        st.markdown("<div class='calorie-container'>", unsafe_allow_html=True)
        st.markdown("#### Calculate your estimated calorie burn.")
        
        # Define exercise MET values (Metabolic Equivalent of Task)
        # These are average values; real values vary greatly.
        met_values = {
            "Running": 8.0,
            "Cycling": 7.5,
            "Swimming": 6.0,
            "Jumping Jacks": 5.0,
            "Squats": 4.0,
            "Mountain Climbers": 6.5,
            "Yoga": 3.0,
            "Walking": 3.5,
        }
        
        col_ex_type, col_ex_weight = st.columns(2)
        with col_ex_type:
            exercise_type = st.selectbox("Choose an activity:", options=list(met_values.keys()))
        with col_ex_weight:
            user_weight = st.number_input("Enter your weight (kg):", min_value=30, max_value=200, value=70)
        
        exercise_duration = st.number_input("Enter duration (minutes):", min_value=1, max_value=180, value=30)

        if st.button("Calculate Calories"):
            met = met_values.get(exercise_type, 1.0) # Default to 1.0 if not found
            # Formula: (MET * 3.5 * weight_in_kg) / 200 * duration_in_minutes
            calories_burned = (met * 3.5 * user_weight) / 200 * exercise_duration
            st.success(f"🔥 Estimated calories burned: **{calories_burned:.0f} kcal**")
        st.markdown("</div>", unsafe_allow_html=True)
        
    st.markdown("---")

    # ----------------- BMI CALCULATOR (IMPROVED STYLING) ------------------
    # Use a container with custom CSS for a more attractive, visible look
    with st.container(border=False):
        st.markdown("<div class='bmi-container'>", unsafe_allow_html=True)
        with st.expander("💖 Click to Calculate Your BMI", expanded=True):
            
            # --- NEW HEIGHT CONVERTER SECTION ---
            with st.expander("💡 Convert Feet & Inches to cm"):
                # Input for feet and inches
                col_ft, col_in = st.columns(2)
                with col_ft:
                    height_ft = st.number_input("Feet:", min_value=1, max_value=8, value=5)
                with col_in:
                    height_in = st.number_input("Inches:", min_value=0, max_value=11, value=9)

                # Calculate the height in centimeters
                cm_from_ft_in = (height_ft * 30.48) + (height_in * 2.54)
                
                # Display the result
                st.info(f"Your height is **{cm_from_ft_in:.2f}** cm. You can use this value above!")
            
            # Using columns to align inputs side-by-side
            col_height, col_weight = st.columns(2)
            with col_height:
                height = st.number_input("📐 Enter your height in cm:", min_value=100, max_value=250, value=165)
            with col_weight:
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
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    
    # ----------------- SMART WATER TRACKER ------------------
    st.markdown("## 💧 Smart Water Tracker")
    with st.container(border=True):
        col_goal, col_input = st.columns(2)
        with col_goal:
            if 'daily_goal' not in st.session_state:
                st.session_state.daily_goal = 2000
            goal_ml = st.number_input("Set your water goal for the day (ml):", 1000, 5000, st.session_state.daily_goal, step=100)
            st.session_state.daily_goal = goal_ml
        
        with col_input:
            new_input = st.number_input("Tell me how much water of the day you drank till now (ml):", 0, 2000, step=50)

        if st.button("📥 Submit"):
            if 'water_drank' not in st.session_state:
                st.session_state.water_drank = 0
            st.session_state.water_drank += new_input
            st.success(f"Recorded: {new_input}ml added to your tracker!")

        drank = st.session_state.water_drank if 'water_drank' in st.session_state else 0
        goal = st.session_state.daily_goal
        
        # Calculate percentage, ensuring it doesn't exceed 100
        percent = int((drank / goal) * 100) if goal > 0 else 0
        if percent > 100: percent = 100
        
        remaining = goal - drank if drank < goal else 0

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

        # --- Dynamic Water Glass & Chart ---
        chart_col, glass_col = st.columns([2, 1])
        with chart_col:
            # Create a simple DataFrame for the bar chart
            chart_df = pd.DataFrame({
                'Water': ['Consumed', 'Remaining'],
                'Milliliters': [drank, remaining]
            })
            st.bar_chart(chart_df, x='Water', y='Milliliters', color='#4dd0e1')
            st.markdown(f"**You have consumed:** `{drank}`ml / `{goal}`ml")
            st.markdown(f"**Remaining:** `{remaining}`ml")
            st.markdown(f"**Current Progress:** `{percent}%`")

        with glass_col:
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
            </style>
            <div class="glass"><div class="water"></div></div>
            """
            st.markdown(glass_html, unsafe_allow_html=True)
            
        st.markdown("---")
            
    # ----------------- WEEKLY PLANNER ------------------
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
    st.dataframe(pd.DataFrame(weekly_plan), use_container_width=True)
    st.info("✅ Pro Tip: Stick to this routine for 3–4 weeks and adjust as needed!")
    st.markdown("---")


    # ----------------- DAILY MOTIVATION (CLEANED UP) ------------------
    st.markdown("## 💬 Daily Motivation")
    with st.container(border=True):
        quotes = [
            "🏋️‍♀️ Push yourself because no one else is going to do it for you.",
            "🔥 Don’t stop when you’re tired, stop when you’re done.",
            "🚀 One workout at a time. One day at a time.",
            "🌟 Strive for progress, not perfection.",
            "🧠 Your body can stand almost anything. It’s your mind that you have to convince.",
            "💡 Little by little, a little becomes a lot.",
        ]
        st.success(random.choice(quotes))
        st.markdown("---")
        st.markdown("### 🎵 Need a boost? Hit the workout playlist!")
        if st.button("▶️ Play Workout Music"):
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=2z8JmcrW-As")


    # ----------------- HABIT TRACKER (CLEANED UP) ------------------
    st.markdown("## 📆 Emoji Habit Tracker - How Was Your Day?")
    with st.container(border=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            water = st.checkbox("💧 Drank enough water?")
            steps = st.checkbox("🚶‍♀️ Walked 5K+ steps?")
        with col2:
            sleep = st.checkbox("😴 Slept 7-8 hours?")
            meals = st.checkbox("🍽️ Ate 3 healthy meals?")
        with col3:
            mood = st.checkbox("😊 Felt happy today?")
        total_done = sum([water, steps, sleep, meals, mood])
        st.markdown(f"### ✅ You completed `{total_done}/5` habits today!")
        st.progress(total_done / 5)
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
    st.markdown("<center><small> Fitness Planner by Tamana Saini</small></center>", unsafe_allow_html=True)


    
# INTERMITTENT FASTING SECTION
elif selected == '🕐 Intermittent Fasting':
    fasting_section()


# CSV TRACKER SECTION
elif selected == '📊 CSV Tracker':
    st.markdown("### 📝 Create Your Fitness Profile")
    st.info("Input your information below to build a personalized CSV file. Data is stored in your session.")

    # Check if a dataframe exists in the session state
    if 'data_df' not in st.session_state:
        st.session_state.data_df = pd.DataFrame(columns=['Name', 'Age', 'Gender', 'Date', 'Weight (kg)', 'Workout Status'])

    with st.form(key='data_entry_form'):
        st.markdown("#### Add New Entry")
        
        # New, properly aligned layout
        col_name, col_age = st.columns(2)
        with col_name:
            name = st.text_input("👤 Your Name", value="", help="Enter your full name.")
        with col_age:
            age = st.number_input("🎂 Your Age", min_value=1, max_value=120, value=25, help="Enter your age in years.")
        
        col_gender, col_date = st.columns(2)
        with col_gender:
            gender = st.radio("🚻 Gender", ('Male', 'Female', 'Non-binary', 'Prefer not to say'), index=3)
        with col_date:
            date = st.date_input("🗓️ Date")

        col_weight, col_workout = st.columns(2)
        with col_weight:
            weight = st.number_input("⚖️ Weight (kg)", min_value=0.0, format="%.1f")
        with col_workout:
            workout_status = st.radio("🏋️ Did workout for the day?", ('Yes', 'No'))
            
        submit_button = st.form_submit_button(label='➕ Add to Tracker')

    if submit_button:
        if not name or not age:
            st.error("Please enter your name and age before submitting.")
        else:
            new_row = {
                'Name': name,
                'Age': age,
                'Gender': gender,
                'Date': date,
                'Weight (kg)': weight,
                'Workout Status': workout_status
            }
            
            # Add the new row to the dataframe
            new_row_df = pd.DataFrame([new_row])
            st.session_state.data_df = pd.concat([st.session_state.data_df, new_row_df], ignore_index=True)
            st.success("Entry added successfully! Scroll down to see your table.")

    st.markdown("---")
    st.markdown("### 📊 Your Recorded Data")
    
    if not st.session_state.data_df.empty:
        st.dataframe(st.session_state.data_df)
        
        # Save and download the data
        csv_data = st.session_state.data_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download Data as CSV",
            data=csv_data,
            file_name=f'fitness_tracker_{name.replace(" ", "_")}.csv',
            mime='text/csv'
        )
    else:
        st.warning("No data has been added yet. Fill out the form above to get started!")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<center><small>Csv Tracer By Tamana Saini</small></center>", unsafe_allow_html=True)

# JUNK TO HEALTHY SECTION
elif selected == '🍟 Junk to Healthy':
    junk_section()


    

# Motivation Footer
st.markdown("<h4 style='text-align: center; color: white;'>DearBody by Tamana: Where wellness meets self-love, one healthy habit at a time. 💖</h4>", unsafe_allow_html=True)
