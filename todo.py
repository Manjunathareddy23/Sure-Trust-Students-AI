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

    # Improved styling
    st.markdown("""
    <style>
        .stApp {
            background-image: url('https://raw.githubusercontent.com/Manjunathareddy23/HACK-WITH-NELLORE-25/main/todo.png');  
            background-size: cover;
            background-position: center;
            height: 100vh;
            color: #FFFFFF;
            font-family: 'Arial', sans-serif;
        }

        .todo-container {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 30px;
            border-radius: 15px;
            width: 80%;
            margin: 20px auto;
            max-width: 600px;
            text-align: center;
            color: #FFFFFF;
        }

        .todo-list li {
            margin: 15px 0;
            background-color: rgba(34, 139, 34, 0.8); /* Green background */
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
            color: #FFF;
        }

        .download-btn {
            background-color: #32CD32;  /* Green button */
            color: #FFFFFF;
            padding: 12px 25px;
            border-radius: 10px;
            margin-top: 20px;
            font-weight: bold;
            cursor: pointer;
            font-size: 16px;
        }

        .todo-input {
            padding: 10px;
            border-radius: 5px;
            font-size: 16px;
            width: 80%;
            margin: 10px 0;
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("To-Do List Generator")
    st.write("Stay organized and track your tasks easily!")

    with st.form("todo_form", clear_on_submit=True):
        todo_item = st.text_input("Enter a new task", max_chars=100)
        add_task_button = st.form_submit_button("Add Task")

    if add_task_button and todo_item:
        if "todo_list" not in st.session_state:
            st.session_state.todo_list = []
        st.session_state.todo_list.append({"task": todo_item, "completed": False})

    if "todo_list" in st.session_state:
        st.markdown('<ul class="todo-list">', unsafe_allow_html=True)
        for idx, task in enumerate(st.session_state.todo_list):
            task_completed = st.checkbox(task['task'], value=task['completed'], key=f"task_{idx}")
            st.session_state.todo_list[idx]['completed'] = task_completed
        st.markdown('</ul>', unsafe_allow_html=True)

        if st.session_state.todo_list:
            pdf_data = generate_pdf(st.session_state.todo_list)
            st.download_button("Download PDF", pdf_data, file_name="todo_list.pdf", mime="application/pdf")

if __name__ == "__main__":
    app()
