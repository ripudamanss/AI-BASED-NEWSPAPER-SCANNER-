import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from ai.chunker import split_articles
from ai.filter import classify
from ocr.extract import extract_text_from_pdf

# -------------------
# App Setup
# -------------------
app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")

# -------------------
# Routes
# -------------------

@app.route("/", methods=["GET"])
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/scan", methods=["GET", "POST"])
def scan():
    if request.method == "GET":
        return "📤 Use POST to upload a PDF file to scan UPSC-relevant news."

    # Save uploaded file
    file = request.files["file"]
    pdf_path = os.path.join(BASE_DIR, "temp.pdf")
    file.save(pdf_path)

    # Extract text
    text = extract_text_from_pdf(pdf_path)

    # Split into articles/chunks
    articles = split_articles(text)

    # Classify
    relevant = []
    for a in articles:
        tags = classify(a)
        if tags:
            relevant.append({
                "text": a[:1000],  # preview only
                "tags": tags
            })

    return jsonify({"relevant_news": relevant})


# -------------------
# Run
# -------------------
if __name__ == "__main__":
    app.run(debug=True)
