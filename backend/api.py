from flask import send_from_directory
from flask import Flask, jsonify, request
from ai.filter import is_relevant 
from ocr.extract import extract_from_url, extract_from_image, extract_text_from_pdf 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return send_from_directory("../frontend", "index.html")


@app.route("/scan", methods=["GET", "POST"])
def scan():
    if request.method == "GET":
        return "📤 Use POST to upload a PDF file to scan UPSC-relevant news."

    file = request.files["file"]
    file.save("temp.pdf")

    text = extract_text_from_pdf("temp.pdf")
    articles = text.split("\n\n")

    relevant = [a for a in articles if is_relevant(a)]

    return jsonify({"relevant_news": relevant})
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return "Welcome to the AI-Based Newspaper Scanner API"

# @app.route('/scan', methods=['POST'])
# def scan():
#     if request.method == "GET":
#         return "📤 Use POST to upload a PDF file to scan UPSC-relevant news."
    
#     file = request.files['file']
#     file.save('temp.pdf')

#     text = extract_text_from_pdf('temp.pdf')
#     articles = text.split('\n\n')

#     relevant = [a for a in articles if is_relevant(a)]
#     return jsonify({"relevant_news": relevant})
