import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

from topsis_logic import topsis_from_file
from email_utils import send_email

# Load environment variables
load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        file = request.files.get("file")
        weights = request.form.get("weights")
        impacts = request.form.get("impacts")
        email = request.form.get("email")

        if not file or file.filename == "":
            return render_template("index.html", message="No file selected")

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        try:
            # Run TOPSIS
            result_path = topsis_from_file(filepath, weights, impacts)

            # Send result via email ✅ FIXED
            send_email(email, result_path)

            message = "TOPSIS analysis completed. Result sent via email."

        except Exception as e:
            message = str(e)

    return render_template("index.html", message=message)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
