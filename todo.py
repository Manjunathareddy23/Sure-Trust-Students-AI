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

    # Add Tailwind CSS for styling and background image
    st.markdown("""
    <style>
        .stApp {
            background-image: url('https://raw.githubusercontent.com/Manjunathareddy23/HACK-WITH-NELLORE-25/main/todo.png');  
            background-size: cover;
            background-position: center;
            height: 100vh;
            color: #FFFFFF;  /* Light text for readability */
            font-family: 'Arial', sans-serif;
        }

        .todo-container {
            background-color: rgba(0, 0, 0, 0.6);  /* Semi-transparent dark background for container */
            padding: 30px;
            border-radius: 15px;
            width: 80%;
            margin: 0 auto;
            max-width: 600px;
            text-align: center;
        }

        h1, h2, h3 {
            color: #FF4500;  /* Vibrant orange for main headings */
            text-align: center;  /* Center align headings */
            font-size: 40px;  /* Increased font size for headings */
        }

        .todo-list {
            margin-top: 20px;
            list-style-type: none;
            padding: 0;
        }

        .todo-list li {
            margin: 15px 0;
            background-color: rgba(255, 223, 0, 0.7);  /* Yellow background for tasks */
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
            color: #333;
            transition: background-color 0.3s ease;
        }

        .todo-list li:hover {
            background-color: rgba(255, 165, 0, 0.8);  /* Slightly orange when hovering */
        }

        .completed {
            text-decoration: line-through;
            color: #808080;
        }

        .download-btn {
            background-color: #FF6347;  /* Vibrant red for the download button */
            color: #000080;  /* Navy blue text color */
            padding: 12px 25px;
            border-radius: 10px;
            text-decoration: none;
            display: inline-block;
            margin-top: 20px;
            font-weight: bold;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        .download-btn:hover {
            background-color: #FF4500;  /* Darker red when hovered */
            color: #87CEEB;  /* Skyblue text color when hovered */
        }

        .todo-input {
            background-color: #fff;
            padding: 10px;
            border-radius: 5px;
            border: none;
            font-size: 16px;
            width: 80%;
            margin: 10px 0;
            text-align: center;  /* Center the input text */
        }

        .todo-input:focus {
            outline: none;
            box-shadow: 0 0 5px rgba(255, 99, 71, 0.7);  /* Add a focus effect */
        }

        .header-text {
            font-size: 48px;  /* Increased font size for header */
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
            color: #FF4500;
            text-align: center;  /* Center the header text */
        }

        .subheader-text {
            font-size: 22px;  /* Increased font size for subheader */
            color: #FF6347;  /* Light red for subheader */
            margin-top: -10px;
            font-weight: 300;
            text-align: center;  /* Center the subheader text */
        }
    </style>
    """, unsafe_allow_html=True)

    # Title and description
    st.title("To-Do List Generator")
    st.markdown('<p class="header-text">Create your to-do list, mark tasks as completed, and download it as a PDF</p>', unsafe_allow_html=True)
    st.markdown('<p class="subheader-text">Stay organized and track your tasks easily!</p>', unsafe_allow_html=True)

    # Input for tasks
    with st.form("todo_form", clear_on_submit=True):
        todo_item = st.text_input("Add a task", key="task_input", placeholder="Enter a new task", label_visibility="collapsed")
        add_task_button = st.form_submit_button("Add Task")

    if add_task_button and todo_item:
        if "todo_list" not in st.session_state:
            st.session_state.todo_list = []
        
        # Add task with completion status set to False
        st.session_state.todo_list.append({"task": todo_item, "completed": False})
    
    # Display the to-do list with checkboxes for completion
    if "todo_list" in st.session_state:
        st.markdown('<div class="todo-container">', unsafe_allow_html=True)
        st.write("### Your To-Do List")
        st.markdown('<ul class="todo-list">', unsafe_allow_html=True)
        
        for idx, task in enumerate(st.session_state.todo_list):
            # Display task with the completion checkbox
            checkbox_label = task["task"]
            if task["completed"]:
                checkbox_label = f'<span class="completed">{task["task"]}</span>'
            
            # Add checkbox for completion status
            task_completed = st.checkbox(checkbox_label, value=task["completed"], key=f"task_{idx}")

            # Update task completion status
            if task_completed != task["completed"]:
                st.session_state.todo_list[idx]["completed"] = task_completed

        st.markdown('</ul>', unsafe_allow_html=True)

        # Button to download the list as a PDF
        if st.session_state.todo_list:
            pdf_data = generate_pdf(st.session_state.todo_list)
            st.download_button("Download PDF", pdf_data, file_name="todo_list.pdf", mime="application/pdf", use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
