import streamlit as st
import pandas as pd
import os

def csv_section():
    st.markdown("<h2 style='text-align: center; color: #FF69B4;'>💾 Health Data Entry & Tracker</h2>", unsafe_allow_html=True)

    # Define the CSV file path
    csv_file = "user_data.csv"

    # Load existing data if file exists
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
    else:
        df = pd.DataFrame(columns=["Name", "Age", "Gender", "Mood", "Weight", "Water Intake", "Goal"])

    # Input section
    with st.form(key="health_form"):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("👤 Name")
            age = st.number_input("🎂 Age", min_value=1, step=1)
            gender = st.selectbox("⚧️ Gender", ["Male", "Female", "Other"])

        with col2:
            mood = st.selectbox("😊 Mood Today", ["Happy", "Tired", "Energetic", "Sad", "Neutral"])
            weight = st.number_input("⚖️ Current Weight (kg)", min_value=1.0, step=0.1)
            water = st.number_input("💧 Water Intake (glasses)", min_value=0, step=1)

        goal = st.selectbox("🎯 Your Health Goal", ["Lose Weight", "Gain Muscle", "Stay Fit", "Improve Energy", "Other"])
        submit = st.form_submit_button("✅ Submit")

    # Save to CSV
    if submit:
        new_data = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Mood": mood,
            "Weight": weight,
            "Water Intake": water,
            "Goal": goal
        }
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        df.to_csv(csv_file, index=False)
        st.success("🎉 Your data has been saved!")
        st.rerun()  # Refresh to show updated data

    # Display existing data
    if not df.empty:
        st.markdown("<h4 style='text-align: center;'>📊 Your Submitted Data</h4>", unsafe_allow_html=True)
        st.dataframe(df.style.highlight_max(axis=0, color="lightgreen"))

    else:
        st.info("No entries yet. Fill the form above to get started.")

