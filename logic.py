import pandas as pd
from datetime import date, timedelta

def generate_full_schedule(subject_data):
    today = date.today()
    schedule_list = []
    
    # Sort subjects by exam date
    subject_data.sort(key=lambda x: x['date'])
    
    # We will plan for the next 15 days
    for i in range(15):
        current_date = today + timedelta(days=i)
        
        # Filter subjects that haven't happened yet
        upcoming = [s for s in subject_data if s['date'] > current_date]
        
        if not upcoming:
            break
            
        # Instead of just the first one, we rotate based on the day
        # This ensures you study a different subject every day
        subject_index = i % len(upcoming)
        target = upcoming[subject_index]
        
        days_left = (target['date'] - current_date).days
        
        # Calculate hours: Difficulty + Urgency
        hours = round((target['difficulty'] * 0.5) + (12 / days_left), 1)
        if hours > 8: hours = 8 
        
        schedule_list.append({
            "Date": current_date.strftime("%Y-%m-%d"),
            "Day": current_date.strftime("%A"),
            "Subject to Study": target['name'],
            "Duration": f"{hours} Hours",
            "Exam Countdown": f"{days_left} Days left"
        })
        
    return pd.DataFrame(schedule_list)