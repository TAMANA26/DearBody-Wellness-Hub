import streamlit as st
from datetime import datetime, timedelta
import time
import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.mplot3d import Axes3D

def fasting_section():
    st.markdown("""
    <style>
    /* Main Container for Fasting Section */
    .fasting-container {
        padding: 01px;
        border-radius: 03;
        margin: 1x 0;
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
    .stSelectbox label, .stNumberInput label {
        color: #4a148c;
        font-weight: bold;
    }

    /* Animated Progress Timer Circle */
    .timer-circle {
        position: relative;
        width: 280px;
        height: 280px;
        border-radius: 50%;
        margin: 30px auto;
        display: flex;
        align-items: center;
        justify-content: center;
        background: conic-gradient(
            #f73b64 var(--progress), /* Start color */
            #ff4081 var(--progress), /* Mid color */
            #e9ecef var(--progress) /* End color */
        );
        box-shadow: inset 0 0 20px rgba(0,0,0,0.1);
        transition: background 1s ease-in-out;
    }
    .timer-inner {
        width: 240px;
        height: 240px;
        background: linear-gradient(145deg, #ffffff, #f0f2f5);
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.05), 0 4px 20px rgba(0,0,0,0.1);
    }
    .timer-time {
        font-size: 3.5rem;
        font-weight: bold;
        color: #4a148c;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }
    .timer-label {
        font-size: 1.2rem;
        color: #6c757d;
        margin-top: 5px;
    }

    /* Milestone and Info Cards */
    .info-card, .milestone-card {
        padding: 25px;
        border-radius: 15px;
        margin-top: 25px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        transition: transform 0.3s;
    }
    .info-card:hover, .milestone-card:hover {
        transform: translateY(-5px);
    }
    .info-card.benefit {
        background: #e1f5fe;
        border-left: 5px solid #039be5;
    }
    .info-card.faq {
        background: #f1f8e9;
        border-left: 5px solid #8bc34a;
    }
    .milestone-card {
        background: #fff8e1;
        border-left: 5px solid #ffb300;
        font-style: italic;
    }
    /* Custom style for attractive expander content */
    .attractive-expander-content {
        background-color: #f0e6f7;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #673ab7;
        margin-top: 10px;
    }
    .attractive-expander-content h4 {
        color: #4a148c;
        font-weight: bold;
        margin-top: 0;
    }
    .attractive-expander-content p {
        margin-bottom: 5px;
    }

    /* Custom separator style */
    .section-separator {
        border-bottom: 2px dashed #ccc;
        margin: 40px 0;
    }
    
    .schedule-card {
      background-color: #f8f9fa;
      border-radius: 8px;
      padding: 15px;
      margin-bottom: 10px;
      border: 1px solid #e9ecef;
    }
    .schedule-card h4 {
      color: #343a40;
      margin-top: 0;
      margin-bottom: 5px;
    }
    .schedule-card p {
      color: #6c757d;
      margin-bottom: 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="fasting-container">', unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center;'>⏳ Your Fasting Journey</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555;'>Track your progress and unlock the amazing benefits of intermittent fasting.</p>", unsafe_allow_html=True)

    # Initialize session state
    if 'is_fasting' not in st.session_state:
        st.session_state.is_fasting = False
    if 'fast_start_time' not in st.session_state:
        st.session_state.fast_start_time = None
    if 'fasting_history' not in st.session_state:
        st.session_state.fasting_history = []
    if 'user_name' not in st.session_state:
        st.session_state.user_name = ""
    
    # Get user's name
    user_name_input = st.text_input("Enter your name:", st.session_state.user_name)
    st.session_state.user_name = user_name_input
    
    # Fasting schedule selection
    schedule_options = {
        "16:8 (Beginner-Friendly)": 16,
        "18:6 (Intermediate)": 18,
        "20:4 (Advanced)": 20,
        "Test Fast (15 seconds)": 15 / 3600,
        "Test Fast (30 seconds)": 30 / 3600
    }
    selected_schedule = st.selectbox(
        "Choose your fasting schedule:",
        list(schedule_options.keys())
    )
    
    # Attractive explanation of schedules
    with st.expander("✨ What do these schedules mean?"):
        st.markdown("""
            <div class="schedule-card">
                <h4>⏰ 16:8 - The Gentle Start</h4>
                <p>You <b>fast for 16 hours</b> and have an <b>8-hour eating window</b>. This is the most popular and beginner-friendly method!</p>
            </div>
            <div class="schedule-card">
                <h4>⚡️ 18:6 - The Next Step</h4>
                <p>You <b>fast for 18 hours</b>, with a shorter <b>6-hour eating window</b>. A great option for intermediate fasters seeking greater benefits.</p>
            </div>
            <div class="schedule-card">
                <h4>⚔️ 20:4 - The Warrior Fast</h4>
                <p>You <b>fast for 20 hours</b>, leaving a concentrated <b>4-hour eating window</b>. An advanced option for those comfortable with longer fasting periods.</p>
            </div>
        """, unsafe_allow_html=True)

    fasting_duration_hours = schedule_options[selected_schedule]
    eating_duration_hours = 24 - fasting_duration_hours
    
    if st.session_state.is_fasting:
        # Determine the fast duration based on the selected schedule
        fast_duration_td = timedelta(hours=fasting_duration_hours)
        if selected_schedule == "Test Fast (15 seconds)":
            fast_duration_td = timedelta(seconds=15)
        elif selected_schedule == "Test Fast (30 seconds)":
            fast_duration_td = timedelta(seconds=30)
            
        elapsed_time = datetime.now() - st.session_state.fast_start_time
        remaining_time = fast_duration_td - elapsed_time

        if remaining_time.total_seconds() <= 0:
            st.session_state.is_fasting = False
            end_time = datetime.now()
            duration = end_time - st.session_state.fast_start_time
            st.session_state.fasting_history.append({
                "name": st.session_state.user_name,
                "schedule": selected_schedule,
                "start": st.session_state.fast_start_time.strftime('%Y-%m-%d %H:%M:%S'),
                "end": end_time.strftime('%Y-%m-%d %H:%M:%S'),
                "duration": str(duration).split('.')[0] 
            })
            st.session_state.fast_start_time = None
            st.balloons()
            st.success(f"🎉 Your fast is complete! Time to enjoy your eating window. 🥳")
            st.rerun()
            
        else:
            fasted_seconds = elapsed_time.total_seconds()
            remaining_seconds = remaining_time.total_seconds()
            progress_percent = (fasted_seconds / (fasted_seconds + remaining_seconds)) * 100
            
            fasted_hours = int(fasted_seconds // 3600)
            fasted_minutes = int((fasted_seconds % 3600) // 60)
            
            rem_minutes, rem_seconds = divmod(int(remaining_seconds), 60)
            rem_hours, rem_minutes = divmod(rem_minutes, 60)
            remaining_str = f"{rem_hours:02d}:{rem_minutes:02d}:{rem_seconds:02d}"

            st.markdown(f"""
            <div class="timer-circle" style="--progress: {progress_percent}%;">
                <div class="timer-inner">
                    <div class="timer-time">{remaining_str}</div>
                    <div class="timer-label">Time Remaining</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            milestones = {
                "0-4": "Post-absorptive state: Your body is digesting food. Energy comes from glucose.",
                "4-8": "Early fasted state: Insulin levels are dropping, and your body starts to burn stored glycogen.",
                "8-12": "Glycogen depletion: Your liver's glycogen stores are low. The body is preparing to burn fat.",
                "12-16": "Ketosis begins: Your body starts producing ketones from fat, a powerful alternative fuel source. Autophagy is kicking in!",
                "16-20": "Deeper ketosis and autophagy: Cellular cleanup is in full swing, repairing and recycling damaged components.",
                "20+": "Advanced fat burning: Your body is a metabolic engine, running primarily on fat for sustained energy."
            }
            
            current_milestone = ""
            if fasted_hours < 4: current_milestone = milestones["0-4"]
            elif fasted_hours < 8: current_milestone = milestones["4-8"]
            elif fasted_hours < 12: current_milestone = milestones["8-12"]
            elif fasted_hours < 16: current_milestone = milestones["12-16"]
            elif fasted_hours < 20: current_milestone = milestones["16-20"]
            else: current_milestone = milestones["20+"]

            st.markdown(f'<div class="milestone-card"><b>Current Stage:</b> {current_milestone}</div>', unsafe_allow_html=True)
            
            st.markdown(f"<p style='text-align: center; margin-top: 20px;'>You have fasted for **{fasted_hours} hours and {fasted_minutes} minutes**.</p>", unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("🛑 End Fast"):
                    st.session_state.is_fasting = False
                    st.session_state.fast_start_time = None
                    st.warning("Fasting session ended early.")
                    st.rerun()
            with col2:
                st.button("🔄 Refresh Timer")
            
            time.sleep(1)
            st.rerun()
            
    else:
        st.markdown("### Ready to Start a New Fast? 🚀")
        if st.button(f"▶️ Start Fast Now", key="start_fast"):
            if not st.session_state.user_name:
                st.error("Please enter your name before starting a fast.")
            else:
                st.session_state.is_fasting = True
                st.session_state.fast_start_time = datetime.now()
                st.success("Fast started successfully! The timer is running.")
                st.rerun()

    st.markdown('<div class="section-separator"></div>', unsafe_allow_html=True)
    
    # WHY INTERMITTENT FASTING SECTION
    st.markdown("### ✨ Why Intermittent Fasting?")
    st.markdown("<p style='text-align: center; color: #555;'>Discover the core benefits that make IF a powerful health tool.</p>", unsafe_allow_html=True)
    
    benefits = [
        ("🔥 Boosts Metabolism", "By improving insulin sensitivity and balancing hormones, IF helps your body become more efficient at burning fat."),
        ("🧠 Enhances Brain Health", "Fasting promotes the growth of new brain cells and can protect against neurodegenerative diseases like Alzheimer's."),
        ("🔬 Cellular Repair", "Autophagy, a process of cellular 'cleanup,' is activated during fasting, which helps remove damaged cells and promote renewal."),
        ("⚖️ Weight Management", "IF can help you lose weight by reducing calorie intake and boosting metabolism, without the need for strict calorie counting."),
    ]
    
    cols = st.columns(len(benefits))
    for i, (title, desc) in enumerate(benefits):
        with cols[i]:
            st.markdown(f'<div class="info-card benefit"><b>{title}</b><p>{desc}</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-separator"></div>', unsafe_allow_html=True)

    # FAQ SECTION
    st.markdown("### ❓ Your Common Questions, Answered")
    
    faqs = {
        "What can I drink during my fast?": "You can drink water, black coffee, or plain tea. These beverages have no calories and won't break your fast.",
        "Will I lose muscle mass?": "No, studies show that IF can help preserve muscle mass while targeting fat for energy, especially when combined with resistance training.",
        "Is intermittent fasting for everyone?": "It's best to consult a doctor before starting IF, especially if you have a medical condition, are pregnant, or have a history of eating disorders.",
    }
    
    for question, answer in faqs.items():
        with st.expander(f"**{question}**"):
            st.markdown(f'<div class="info-card faq"><p>{answer}</p></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-separator"></div>', unsafe_allow_html=True)

    # FASTING HISTORY
    st.markdown("### 📜 Your Fasting History")
    if 'fasting_history' in st.session_state and st.session_state.fasting_history:
        history_df = pd.DataFrame(st.session_state.fasting_history)
        # Reorder columns to put name first
        cols = ["name", "schedule", "start", "end", "duration"]
        if "schedule" not in history_df.columns:
            cols.remove("schedule")
        
        st.dataframe(history_df[cols], use_container_width=True)
        if st.button("🗑️ Clear History"):
            st.session_state.fasting_history = []
            st.success("Fasting history cleared!")
            st.rerun()
    else:
        st.info("Your fasting history will appear here once you complete your first fast!")
    
    st.markdown("</div>", unsafe_allow_html=True)