TOPSIS Web Service

📌 Project Overview

This project implements TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) as a web service using Flask.
Users can upload a CSV file, specify weights and impacts, and receive the ranked result via email.

The application is deployed on Render using Gunicorn as a production WSGI server.

🚀 Live Demo

🔗 Deployed URL:
https://topsis-web-service-r3b8.onrender.com

🧠 Features

Upload CSV file containing alternatives and criteria

Accept weights and impacts from user

Validate inputs (weights, impacts, email)

Compute TOPSIS score and rank

Generate result CSV file

Send result to user via email

Clean, responsive UI (Tailwind CSS)

Production deployment on Render

🛠️ Tech Stack

Backend: Python, Flask

Frontend: HTML, Tailwind CSS, JavaScript

Computation: NumPy, Pandas

Email: SMTP (Gmail App Password)

Deployment: Render

WSGI Server: Gunicorn

Version Control: Git & GitHub

📂 Project Structure
topsis-web-service/
│
├── app.py                 # Flask application
├── topsis_logic.py        # TOPSIS computation logic
├── email_utils.py         # Email sending utility
├── requirements.txt       # Python dependencies
├── .gitignore
│
├── templates/
│   └── index.html         # Frontend UI
│
├── static/
│   └── styles.css         # Optional custom styles
│
├── uploads/
│   ├── input.csv
│   └── result.csv

📥 Input Format

CSV File

First column: Alternative names

Remaining columns: Numeric criteria

Weights

1,1,1


Impacts

+,+,-

📤 Output

CSV file containing:

TOPSIS Score

Rank

Sent to the provided email address

🔐 Environment Variables

These must be set locally or on Render Dashboard:

EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password


⚠️ .env file is not committed to GitHub for security.

▶️ Run Locally
git clone https://github.com/Keshav123708/topsis-web-service.git
cd topsis-web-service
pip install -r requirements.txt
python app.py


Open in browser:

http://127.0.0.1:5000

🌐 Deployment (Render)

Platform: Render

Start Command:

gunicorn app:app


Free tier instance used

📘 Academic Notes (Viva Ready)

Flask’s built-in server is for development only

Gunicorn is used for production deployment

Environment variables are used for sensitive credentials

Email delivery improves usability and automation

Project follows modular and clean architecture

👨‍💻 Author

Keshav Sharma
Roll No: 102303520
B.Tech Computer Engineering
Thapar Institute of Engineering & Technology