import streamlit as st
import pandas as pd
from logic import generate_full_schedule
from datetime import date

st.set_page_config(page_title="AI Master Planner", layout="wide")

st.title("📅 Detailed AI Study Planner")
st.write("Enter subjects and number of units to generate a topic-wise schedule.")

if 'subjects' not in st.session_state:
    st.session_state.subjects = []

with st.form("subject_form"):
    col1, col2, col3, col4 = st.columns(4)
    name = col1.text_input("Subject Name")
    units = col2.number_input("Total Units", min_value=1, max_value=10, value=5) # New Input
    exam_dt = col3.date_input("Exam Date", min_value=date.today())
    diff = col4.slider("Difficulty (1-10)", 1, 10, 5)
    
    if st.form_submit_button("Add Subject"):
        if name:
            st.session_state.subjects.append({
                "name": name, 
                "units": int(units), 
                "date": exam_dt, 
                "difficulty": diff
            })
            st.success(f"Added {name} with {units} units")

if st.session_state.subjects:
    st.write("### Added Subjects:")
    st.table(pd.DataFrame(st.session_state.subjects))

    if st.button("Generate My Detailed Timetable"):
        st.write("### 🗓️ Your Unit-wise Study Schedule")
        df_schedule = generate_full_schedule(st.session_state.subjects)
        st.dataframe(df_schedule, use_container_width=True)
        
        if st.button("Clear All"):
            st.session_state.subjects = []
            st.rerun()