# TOPSIS Web Service 

This project is a web-based implementation of **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)**.  
It allows users to upload a CSV file, specify weights and impacts, and obtain TOPSIS scores and rankings through a simple web interface.

---

## 🔹 Features

- Web-based TOPSIS implementation
- CSV file upload for decision matrix
- User-defined weights and impacts
- Automatic TOPSIS score & ranking calculation
- Result generated as a CSV file
- Optional email support (SMTP based)
- Clean and simple UI

---

## 🔹 Tech Stack

- **Backend:** Python, Flask  
- **Computation:** NumPy, Pandas  
- **Frontend:** HTML, CSS  
- **WSGI Server:** Gunicorn  
- **Version Control:** Git & GitHub  

---

## 📁 Project Structure

```text

topsis-web-service/
├── app.py                # Flask application
├── topsis_logic.py       # TOPSIS computation logic
├── email_utils.py        # Email utility
├── requirements.txt      # Python dependencies
├── .gitignore
├── README.md
├── templates/
│   └── index.html        # Web UI
├── static/
│   └── styles.css        # Styling
└── uploads/
    ├── input.csv
    └── result.csv
```



---

## 🔹 Input Format

### CSV File
- First column: Alternative names  
- Remaining columns: Numeric criteria values  

Example:
Model,Cost,Performance,Battery
A,250,80,6
B,200,70,8
C,300,90,7


### Weights
Comma-separated numeric values  
Example:
1,1,1


### Impacts
Use:
- `+` for beneficial criteria
- `-` for cost criteria  

Example:
-,+,+


---

## 🔹 Output

A CSV file containing:
- TOPSIS Score  
- Rank of each alternative  

---

## 🔹 Environment Variables (Optional)

For email functionality:

EMAIL_ADDRESS=your_email@gmail.com

EMAIL_PASSWORD=your_gmail_app_password


> `.env` file is not committed for security reasons.

---

## 🔹 Run Locally

1. Clone repository:
```bash
git clone https://github.com/Keshav123708/topsis-web-service.git

2. Move into project:
cd topsis-web-service

3.Install dependencies:
pip install -r requirements.txt

4. Run application:
python app.py

5.Open browser:
http://127.0.0.1:5000

🔹 Deployment Note

The application is compatible with cloud deployment platforms (e.g., Render).
Free-tier deployments may experience limitations such as service sleep or restricted network access.
This does not affect the core TOPSIS implementation, which works correctly when run locally.

👨‍💻 Developer

Keshav Sharma
B.Tech – Computer Engineering
Thapar Institute of Engineering & Technology