import streamlit as st
import pandas as pd  # <--- THIS WAS MISSING
from logic import generate_full_schedule
from datetime import date

# Page Configuration
st.set_page_config(page_title="AI Master Planner", layout="wide")

st.title("📅 Multi-Subject Exam Planner")
st.write("Enter your subjects and exam dates to generate your full study timetable.")

# Create a list to store subject info in the session
if 'subjects' not in st.session_state:
    st.session_state.subjects = []

# Input Section
with st.form("subject_form"):
    col1, col2, col3 = st.columns(3)
    name = col1.text_input("Subject Name")
    exam_dt = col2.date_input("Exam Date", min_value=date.today())
    diff = col3.slider("Difficulty (1-10)", 1, 10, 5)
    
    if st.form_submit_button("Add Subject"):
        if name:
            st.session_state.subjects.append({"name": name, "date": exam_dt, "difficulty": diff})
            st.success(f"Added {name}")

# Show current list
if st.session_state.subjects:
    st.write("### Added Subjects:")
    # Now pd.DataFrame will work!
    st.table(pd.DataFrame(st.session_state.subjects))

    if st.button("Generate My Full Timetable"):
        st.write("### 🗓️ Your Optimized Study Schedule")
        df_schedule = generate_full_schedule(st.session_state.subjects)
        
        # Display the dataframe nicely
        st.dataframe(df_schedule, use_container_width=True)