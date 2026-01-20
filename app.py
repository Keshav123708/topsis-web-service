from topsis_logic import topsis_from_file
from flask import Flask, render_template, request
import os
from topsis_logic import topsis_from_file
from email_utils import send_email

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
            result_path = topsis_from_file(filepath, weights, impacts)
            send_email(email, result_path)
            message = "TOPSIS analysis completed. Result sent via email."
        except Exception as e:
            message = str(e)

    return render_template("index.html", message=message)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
