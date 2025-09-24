# Sure-Trust-Students-AI

A student-centered AI web app project (built in Python / Flask) for managing schedules, summaries, to-dos, and more.  

## 📁 Project Structure

Sure-Trust-Students-AI/
├── app.py
├── requirements.txt
├── pages/
├── assets/
├── summary.py
├── timetable.py
├── todo.py
├── utube.py
├── lang.py
├── entry.jpg
├── lang.jpg
├── summary.jpg
├── time.jpg
├── todo.png
└── .env

markdown
Copy code

## 🛠️ Features

- View and manage students’ timetables (`timetable.py`)  
- Generate summaries of text (`summary.py`)  
- Create and manage to-do lists (`todo.py`)  
- Integrate with YouTube / embedding via `utube.py`  
- Language processing features via `lang.py`  
- Web interface and routing handled in `app.py`  
- Static assets and pages stored in `assets/` and `pages/`  
- Environment configuration stored in `.env`

## 🚀 Setup & Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Manjunathareddy23/Sure-Trust-Students-AI.git
   cd Sure-Trust-Students-AI
Create a Python virtual environment (recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Setup environment variables in .env (if needed). For example:

text
Copy code
FLASK_APP=app.py
FLASK_ENV=development
Run the app:

bash
Copy code
flask run
Open your browser and go to http://127.0.0.1:5000

🧪 Usage Examples
Navigate to different pages via the web UI (e.g. /summary, /todo, /timetable)

Enter or upload content to generate summaries

Add tasks to to-do lists and mark them done

Visualize time schedules

Use language processing or YouTube embedding features

📦 Dependencies
See requirements.txt for a full list of required Python packages.



🛡️ License & Contribution
This project is open-source. Feel free to fork, contribute, or raise issues.

Before contributing, please ensure to follow the project’s coding style and test your changes.
