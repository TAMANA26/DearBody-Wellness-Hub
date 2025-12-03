import os
import pandas as pd
from datetime import datetime

def get_log_file_path():
    return os.path.join("data", "user_logs.csv")

def log_user_entry(name, goal, mood, date, water_intake, exercise_done):
    file_path = get_log_file_path()

    new_entry = {
        "Name": name,
        "Goal": goal,
        "Mood": mood,
        "Date": date,
        "Water Intake (L)": water_intake,
        "Exercise Done": exercise_done,
        "Logged At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if not os.path.exists(file_path):
        df = pd.DataFrame([new_entry])
        df.to_csv(file_path, index=False)
    else:
        df = pd.read_csv(file_path)
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        try:
            df.to_csv(file_path, index=False)
        except PermissionError:
            raise PermissionError("⚠️ Please close the user_logs.csv file before saving.")
