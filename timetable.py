import streamlit as st
from fpdf import FPDF
import pandas as pd

# Set Streamlit page configuration
st.set_page_config(page_title="Student Timetable Planner", page_icon="📅", layout="wide")

# Custom CSS for styling
st.markdown('''
    <style>
        body {
            background-color: #f0f4f8;
            font-family: Arial, sans-serif;
        }
        h1 {
            text-align: center;
            color: #4CAF50;
            text-shadow: 2px 2px 4px #000000;
            margin-bottom: 30px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        }
        th, td {
            border: 2px solid #32CD32;
            padding: 12px;
            text-align: center;
            font-size: 16px;
            color: #333;
            background-color: #fff;
            text-shadow: 1px 1px 2px #aaa;
        }
        th {
            background-color: #32CD32;
            color: white;
            font-size: 18px;
            text-shadow: 1px 1px 2px #000;
        }
        .download-btn {
            background-color: #FF1493;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: bold;
            margin-top: 20px;
            cursor: pointer;
            transition: 0.3s;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
        }
        .download-btn:hover {
            background-color: #D6006E;
        }
    </style>
''', unsafe_allow_html=True)

st.title("📅 Student Timetable Planner")

# Input collection
task_data = []
num_tasks = st.number_input("Enter the number of tasks:", min_value=1, max_value=10, step=1)

for i in range(num_tasks):
    st.subheader(f"Task {i + 1}")
    task_name = st.text_input(f"Enter task name for Task {i + 1}:")
    start_time = st.text_input(f"Start time for {task_name} (e.g., 9:00 AM):")
    end_time = st.text_input(f"End time for {task_name} (e.g., 10:00 AM):")
    duration = st.text_input(f"Duration for {task_name} (in hours):")
    task_data.append([task_name, start_time, end_time, duration])

# Display and download timetable
if st.button("Generate Timetable"):
    df = pd.DataFrame(task_data, columns=["Task", "Start Time", "End Time", "Duration (hrs)"])
    st.table(df)

    # PDF Generation
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Student Timetable", ln=True, align='C')
    pdf.ln(10)
    for task in task_data:
        pdf.cell(200, 10, txt=f"Task: {task[0]} | Start: {task[1]} | End: {task[2]} | Duration: {task[3]} hrs", ln=True)
    pdf_data = pdf.output(dest="S").encode("latin1")
    st.download_button("Download Timetable as PDF", pdf_data, "timetable.pdf", mime="application/pdf")
