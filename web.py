from flask import Flask, render_template, request
import requests
import base64
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_URL = os.getenv("HUGGING_FACE_API_URL")
API_KEY = os.getenv("HUGGING_FACE_API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/octet-stream"
}


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "file1" not in request.files:
        return "No file selected", 400

    file_storage = request.files["file1"]
    file_bytes = file_storage.read()

    response = requests.post(API_URL, headers=headers, data=file_bytes)

    if response.status_code != 200:
        return f"Hugging Face error {response.status_code}: {response.text}", 500

    try:
        model_results = response.json()
    except ValueError:
        return f"Invalid response from Hugging Face: {response.text}", 500

    if isinstance(model_results, dict) and "error" in model_results:
        return f"Model error: {model_results['error']}", 500

    top_result = model_results[0]
    is_hotdog = top_result["label"].lower() == "hot dog"
    score = round(top_result["score"] * 100, 2)

    encoded_image = base64.b64encode(file_bytes).decode("utf-8")

    return render_template(
        "result.html",
        is_hotdog=is_hotdog,
        score=score,
        img_data=encoded_image
    )


if __name__ == "__main__":
    app.run(debug=True)





    
    