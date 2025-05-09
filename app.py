import streamlit as st

# Page configuration
st.set_page_config(page_title="Manju's Productivity Suite", page_icon="🚀")

# Initialize session state for navigation
if "selected_tool" not in st.session_state:
    st.session_state.selected_tool = "Home"

# Function to handle navigation
def set_tool(tool_name):
    st.session_state.selected_tool = tool_name

# Inject Custom CSS for Header Nav
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }

    .nav-bar {
        display: flex;
        justify-content: space-around;
        background-color: rgba(255,255,255,0.05);
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    .nav-bar button {
        background-color: rgba(255,255,255,0.1);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        transition: 0.3s;
        cursor: pointer;
    }

    .nav-bar button:hover {
        background-color: rgba(255,255,255,0.2);
        transform: scale(1.05);
    }

    .title-box {
        padding: 20px;
        border-radius: 20px;
        background: linear-gradient(145deg, #1e3c72, #2a5298);
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
        text-align: center;
        margin-bottom: 30px;
        transition: transform 0.5s ease, box-shadow 0.5s ease;
    }

    .title-box:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 30px rgba(0,0,0,0.6);
    }
    </style>
""", unsafe_allow_html=True)

# Title section
st.markdown("""
<div class="title-box">
    <h1>🚀 Manju's Productivity Suite</h1>
</div>
""", unsafe_allow_html=True)

# Header Navigation
st.markdown('<div class="nav-bar">', unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
with col1: st.button("🏠 Home", on_click=set_tool, args=("Home",))
with col2: st.button("📝 To-Do", on_click=set_tool, args=("To-Do",))
with col3: st.button("📅 Timetable", on_click=set_tool, args=("Timetable",))
with col4: st.button("🌍 Translator", on_click=set_tool, args=("Translator",))
with col5: st.button("📄 Summarizer", on_click=set_tool, args=("Summarizer",))
st.markdown('</div>', unsafe_allow_html=True)

# Conditional display based on tool selected
if st.session_state.selected_tool == "Home":
    st.markdown("""
        ### 👋 Choose a tool above to get started!
    """)
elif st.session_state.selected_tool == "To-Do":
    st.markdown("## 📝 To-Do List Generator")
    # Placeholder for your To-Do App logic
elif st.session_state.selected_tool == "Timetable":
    st.markdown("## 📅 Student Timetable Planner")
    # Placeholder for Timetable App logic
elif st.session_state.selected_tool == "Translator":
    st.markdown("## 🌍 Language Translator")
    # Placeholder for Translator App logic
elif st.session_state.selected_tool == "Summarizer":
    st.markdown("## 📄 PDF Summarizer")
    # Placeholder for PDF Summarizer App logic
