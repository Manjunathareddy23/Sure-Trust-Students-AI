import streamlit as st
from fpdf import FPDF

# Function to generate PDF
def generate_pdf(todo_list):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="To-Do List", ln=True, align="C")
    pdf.ln(10)

    for task in todo_list:
        status = "Completed" if task['completed'] else "Pending"
        pdf.cell(200, 10, txt=f"- {task['task']} ({status})", ln=True)

    return pdf.output(dest='S').encode('latin1')

# Streamlit UI Setup
def app():
    st.set_page_config(page_title="To-Do List Generator", page_icon="📝", layout="wide")

    # Styling for vibrant headings, shadow effects, and button fixes
    st.markdown('''
    <style>
        .stApp {
            background-image: url('https://raw.githubusercontent.com/Manjunathareddy23/HACK-WITH-NELLORE-25/main/todo.png');
            background-size: cover;
            background-position: center;
            color: #FFFFFF;
            font-family: Arial, sans-serif;
        }

        .header-text {
            font-size: 48px;
            font-weight: bold;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
            color: #FF6347;
            text-align: center;
            margin-bottom: 10px;
        }

        .subheader-text {
            font-size: 22px;
            font-weight: 300;
            color: #87CEEB;
            text-shadow: 1px 1px 5px rgba(0,0,0,0.5);
            text-align: center;
            margin-bottom: 20px;
        }

        .todo-container {
            background-color: rgba(0, 0, 0, 0.6);
            padding: 30px;
            border-radius: 15px;
            width: 80%;
            margin: 20px auto;
            max-width: 600px;
            color: #FFFFFF;
        }

        .todo-list li {
            margin: 10px 0;
            background-color: rgba(34, 139, 34, 0.8);
            padding: 10px;
            border-radius: 10px;
            color: #FFF;
            font-size: 18px;
            list-style-type: none;
        }

        .download-btn {
            background-color: #32CD32;
            color: #FFFFFF;
            padding: 10px 20px;
            border-radius: 10px;
            font-weight: bold;
            font-size: 16px;
            margin-top: 15px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .download-btn:hover {
            background-color: #228B22;
        }

        .todo-input {
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
            width: 80%;
            font-size: 16px;
        }
    </style>
    ''', unsafe_allow_html=True)

    st.markdown('<h1 class="header-text">To-Do List Generator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subheader-text">Stay organized and track your tasks effectively!</p>', unsafe_allow_html=True)

    with st.form("todo_form", clear_on_submit=True):
        todo_item = st.text_input("Enter a new task", max_chars=100, placeholder="Add a task...")
        add_task_button = st.form_submit_button("Add Task")

    if add_task_button and todo_item:
        if "todo_list" not in st.session_state:
            st.session_state.todo_list = []
        st.session_state.todo_list.append({"task": todo_item, "completed": False})

    if "todo_list" in st.session_state:
        st.markdown('<div class="todo-container">', unsafe_allow_html=True)
        st.write("### Your To-Do List:")
        st.markdown('<ul class="todo-list">', unsafe_allow_html=True)
        for idx, task in enumerate(st.session_state.todo_list):
            task_completed = st.checkbox(task['task'], value=task['completed'], key=f"task_{idx}")
            st.session_state.todo_list[idx]['completed'] = task_completed
        st.markdown('</ul>', unsafe_allow_html=True)

        if st.session_state.todo_list:
            pdf_data = generate_pdf(st.session_state.todo_list)
            st.download_button("Download PDF", pdf_data, file_name="todo_list.pdf", mime="application/pdf", help="Download your to-do list as a PDF")

        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
