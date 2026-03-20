import pandas as pd
from datetime import date, timedelta

def generate_full_schedule(subject_data):
    today = date.today()
    schedule_list = []
    subject_data.sort(key=lambda x: x['date'])
    
    # Unit tracking: Keep track of which unit to study next for each subject
    # Example: {'Physics': 1, 'Maths': 1}
    subject_unit_tracker = {s['name']: 1 for s in subject_data}
    
    for i in range(15):
        current_date = today + timedelta(days=i)
        upcoming = [s for s in subject_data if s['date'] > current_date]
        
        if not upcoming:
            break
            
        subject_index = i % len(upcoming)
        target = upcoming[subject_index]
        
        # Get current unit for this subject
        current_unit = subject_unit_tracker[target['name']]
        total_units = target['units']
        
        days_left = (target['date'] - current_date).days
        hours = round((target['difficulty'] * 0.5) + (12 / days_left), 1)
        if hours > 8: hours = 8 
        
        schedule_list.append({
            "Date": current_date.strftime("%Y-%m-%d"),
            "Day": current_date.strftime("%A"),
            "Subject": target['name'],
            "Topic": f"Unit {current_unit}", # Unit mention
            "Duration": f"{hours} Hours",
            "Exam Countdown": f"{days_left} Days"
        })
        
        # Increment unit for next time this subject appears
        # If it reaches total units, it restarts from Unit 1 for revision
        if current_unit < total_units:
            subject_unit_tracker[target['name']] += 1
        else:
            subject_unit_tracker[target['name']] = 1
            
    return pd.DataFrame(schedule_list)