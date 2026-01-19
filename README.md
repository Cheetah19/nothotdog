# 🌭 Not Hot Dog – Image Classification App

A Flask web application that classifies images as **Hot Dog** or **Not Hot Dog**
using a Machine Learning model via the **Hugging Face Inference API**.

Inspired by the famous *Silicon Valley* TV show.

---

## 🚀 Features
- Upload an image through the browser
- Image classification using an ML model
- Displays prediction confidence
- Simple Flask backend

---

## 🛠 Tech Stack
- Python
- Flask
- HTML
- Hugging Face Inference API

---

## 📂 Project Structure
nothotdog/
│── web.py
│── requirements.txt
│── templates/
│ └── index.html
│── .env
│── README.md


---

## ⚙️ Setup & Run Locally

```bash
git clone https://github.com/yourusername/nothotdog.git
cd nothotdog
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python web.py

🔐 Environment Variables
This project uses environment variables to keep sensitive data secure.
Create a .env file in the project root and add:
HUGGINGFACE_API_KEY=your_huggingface_api_key
You can generate an API key from:
https://huggingface.co/settings/tokens

⚠️ Do not commit the .env file to GitHub.

📌 What I Learned
Basics of Flask backend development
Integrating Machine Learning APIs
Handling environment variables securely
Managing dependencies using requirements.txt
Structuring a Python project

📸 Demo
![alt text](<hotdog result-2.jpeg>)

🔗 Connect with Me

GitHub: https://github.com/Cheetah19

LinkedIn: www.linkedin.com/in/pratyaksha-mishra-4a4093298

---

## 🌱 Note

This is my first end-to-end Flask project, built as part of my learning journey in Python and Machine Learning.

The goal of this project was to understand how backend development, APIs, and basic ML integration work together in a real application.
