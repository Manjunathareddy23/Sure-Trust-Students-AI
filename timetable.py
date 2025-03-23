import streamlit as st
from fpdf import FPDF
import pandas as pd

st.set_page_config(page_title="Student Timetable Planner", page_icon="📅", layout="wide")

# Background image URL
background_url = "https://raw.githubusercontent.com/Manjunathareddy23/HACK-WITH-NELLORE-25/main/time.jpg"

st.markdown(f'''
    <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url('{background_url}');
            background-size: cover;
            background-position: center;
            font-family: Arial, sans-serif;
            color: #FF0000;
        }}
        h1 {{
            text-align: center;
            color: #4CAF50;
            text-shadow: 2px 2px 4px #000000;
            margin-bottom: 30px;
            font-size: 3rem;
            transition: transform 0.3s;
        }}
        h1:hover {{
            transform: scale(1.05);
        }}
        label, .skyblue-text {{
            color: skyblue;
            font-weight: bold;
            font-size: 1.2rem;
            margin-bottom: 8px;
            text-shadow: 1px 1px 2px #000;
        }}
        .task-input {{
            margin-bottom: 20px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.4);
            padding: 15px;
            border-radius: 10px;
            background-color: rgba(255, 255, 255, 0.8);
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
            background-color: rgba(255, 255, 255, 0.9);
        }}
        th, td {{
            border: 2px solid #32CD32;
            padding: 12px;
            text-align: center;
            font-size: 16px;
            background-color: #fff;
            color: #FF0000;
            font-weight: bold;
            transition: transform 0.3s;
        }}
        th:hover, td:hover {{
            transform: scale(1.05);
            color: #000;
        }}
        .download-btn {{
            background-color: #FF1493;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: bold;
            margin-top: 20px;
            cursor: pointer;
            transition: 0.3s;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
        }}
        .download-btn:hover {{
            background-color: #D6006E;
            transform: translateY(-3px);
        }}
    </style>
''', unsafe_allow_html=True)

st.title("📅 Student Timetable Planner")

task_data = []
st.markdown('<p class="skyblue-text">Enter the number of tasks:</p>', unsafe_allow_html=True)
num_tasks = st.number_input("", min_value=1, max_value=10, step=1)

for i in range(num_tasks):
    st.subheader(f"Task {i + 1}")
    
    # Task Name
    st.markdown(f'<p class="skyblue-text">Enter task name for Task {i + 1}:</p>', unsafe_allow_html=True)
    task_name = st.text_input("", key=f"task_name_{i}")

    # Start Time
    st.markdown(f'<p class="skyblue-text">Start time for {task_name} (e.g., 9:00 AM):</p>', unsafe_allow_html=True)
    start_time = st.text_input("", key=f"start_time_{i}")

    # End Time
    st.markdown(f'<p class="skyblue-text">End time for {task_name} (e.g., 10:00 AM):</p>', unsafe_allow_html=True)
    end_time = st.text_input("", key=f"end_time_{i}")

    # Duration
    st.markdown(f'<p class="skyblue-text">Duration for {task_name} (in hours):</p>', unsafe_allow_html=True)
    duration = st.text_input("", key=f"duration_{i}")

    if task_name and start_time and end_time and duration:
        task_data.append([task_name, start_time, end_time, duration])

if st.button("Generate Timetable") and task_data:
    df = pd.DataFrame(task_data, columns=["Task", "Start Time", "End Time", "Duration (hrs)"])
    st.table(df)

    # Generate PDF with formatted table
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "Student Timetable", ln=True, align='C')
    pdf.ln(10)

    # Header
    pdf.set_font("Arial", "B", 12)
    pdf.set_fill_color(50, 205, 50)  # Green
    pdf.set_text_color(255, 255, 255)  # White
    pdf.cell(50, 10, "Task", border=1, fill=True, align='C')
    pdf.cell(40, 10, "Start Time", border=1, fill=True, align='C')
    pdf.cell(40, 10, "End Time", border=1, fill=True, align='C')
    pdf.cell(40, 10, "Duration (hrs)", border=1, fill=True, align='C')
    pdf.ln()

    # Data Rows
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)  # Black
    for task in task_data:
        pdf.cell(50, 10, task[0], border=1, align='C')
        pdf.cell(40, 10, task[1], border=1, align='C')
        pdf.cell(40, 10, task[2], border=1, align='C')
        pdf.cell(40, 10, task[3], border=1, align='C')
        pdf.ln()

    pdf_data = pdf.output(dest="S").encode("latin1")
    st.download_button("Download Timetable as PDF", pdf_data, "timetable.pdf", mime="application/pdf", key="download_pdf")
