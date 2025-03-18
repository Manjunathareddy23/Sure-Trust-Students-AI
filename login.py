# login.py
import streamlit as st
import app  # Import the main app for redirection

# --- Helper functions for Variable-based login ---
valid_users = {
    '22G21A0593': '22G21A0593',  # Reg Number as both username and password
    '22G21A05C5': '22G21A05C5',
    '22G21A05A0': '22G21A05A0',
    # Add more users as needed
}

def validate_login(username, password):
    try:
        # Check if the username exists and the password matches
        if username in valid_users:
            if valid_users[username] == password:
                return True
            else:
                st.error("Invalid Password!")
                return False
        else:
            st.error("User not found!")
            return False
    except Exception as e:
        st.error(f"An error occurred while validating login: {e}")
        return False

def login_page():
    st.markdown("""
        <style>
            .stButton>button {
                background-color: #1D4ED8;
                color: white;
                border-radius: 8px;
                padding: 12px 24px;
                font-size: 16px;
                transition: background-color 0.3s;
            }
            .stButton>button:hover {
                background-color: #2563EB;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title('Login Page')

    username = st.text_input('Username (Reg Number)', placeholder="Enter your Reg Number", max_chars=10)
    password = st.text_input('Password (Reg Number)', type='password', placeholder="Enter your Reg Number", max_chars=10)

    if st.button('Login'):
        if validate_login(username, password):
            st.success('Login Successful')
            st.session_state.logged_in = True  # Set the session state flag to indicate login success
            st.experimental_rerun()  # Reload the page to switch to the main app
        else:
            st.error('Invalid Username or Password')

if __name__ == "__main__":
    login_page()  # Show login page initially
