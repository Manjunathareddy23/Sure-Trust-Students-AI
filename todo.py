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

    for item in todo_list:
        pdf.cell(200, 10, txt=f"- {item}", ln=True)

    return pdf.output(dest='S').encode('latin1')

# Streamlit UI Setup
def app():
    st.set_page_config(page_title="To-Do List Generator", page_icon="📝", layout="wide")

    # Add Tailwind CSS for styling and background image
    st.markdown("""
    <style>
        .stApp {
            background-image: url('https://example.com/your-image.jpg');
            background-size: cover;
            background-position: center;
            height: 100vh;
            color: white;
        }
        .todo-container {
            background-color: rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 10px;
            width: 80%;
            margin: 0 auto;
            max-width: 500px;
            text-align: center;
        }
        .todo-list {
            margin-top: 10px;
            list-style-type: none;
            padding: 0;
        }
        .todo-list li {
            margin: 10px 0;
            background-color: rgba(255, 255, 255, 0.7);
            padding: 10px;
            border-radius: 5px;
        }
        .download-btn {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            display: inline-block;
            margin-top: 20px;
            font-weight: bold;
            cursor: pointer;
        }
        .download-btn:hover {
            background-color: #45a049;
        }
    </style>
    """, unsafe_allow_html=True)

    # Title and description
    st.title("To-Do List Generator")
    st.write("Create your to-do list and download it as a PDF")

    # Input for tasks
    with st.form("todo_form", clear_on_submit=True):
        todo_item = st.text_input("Add a task")
        add_task_button = st.form_submit_button("Add Task")

    if add_task_button and todo_item:
        if "todo_list" not in st.session_state:
            st.session_state.todo_list = []
        
        st.session_state.todo_list.append(todo_item)
    
    # Display the to-do list
    if "todo_list" in st.session_state:
        st.markdown('<div class="todo-container">', unsafe_allow_html=True)
        st.write("### Your To-Do List")
        st.markdown('<ul class="todo-list">', unsafe_allow_html=True)
        for item in st.session_state.todo_list:
            st.markdown(f'<li>{item}</li>', unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)

        # Button to download the list as a PDF
        if st.session_state.todo_list:
            pdf_data = generate_pdf(st.session_state.todo_list)
            st.download_button("Download PDF", pdf_data, file_name="todo_list.pdf", mime="application/pdf")

        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
