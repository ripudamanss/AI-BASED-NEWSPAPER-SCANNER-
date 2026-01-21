# 📰 AI-Based UPSC Newspaper Scanner

An intelligent AI-powered tool that scans newspapers (PDFs, images, or web articles) and filters only **UPSC Prelims & Mains syllabus-relevant news** — cutting out distractions and saving serious study time.

Built for aspirants who want **signal over noise**.

---

## 🚀 Features

* 📄 **PDF, Image & Website Support**
* 🔍 **AI-Powered Relevance Detection** (Syllabus-Based Filtering)
* 🧠 **Semantic Understanding** (Not Just Keyword Matching)
* 🗂️ **Auto-Categorization**

  * Polity
  * Economy
  * Environment
  * International Relations
  * Science & Technology
* 📝 **Optional One-Line Notes Generator**
* 📤 **Export Filtered News as PDF / TXT for Revision**

---

## 🎯 Why This Project?

UPSC aspirants spend **2–3 hours daily** filtering newspapers manually.

This tool:

* Cuts reading time by **60–70%**
* Improves focus on **exam-relevant content**
* Builds **daily digital notes automatically**
  
---

## 🧠 How It Works

### 1️⃣ Input

Supports:

* Newspaper PDFs
* Scanned Images
* Website Links

### 2️⃣ Text Extraction

* PDF → `pdfplumber`
* Image → `Tesseract OCR`
* Website → `BeautifulSoup`

### 3️⃣ AI Filtering Engine

* Matches articles with UPSC syllabus using:

  * Keyword Filtering (Fast Layer)
  * Sentence Transformers (Semantic Layer)

### 4️⃣ Output

* Displays only relevant articles
* Groups them by subject
* Generates optional notes

---

## 🏗️ Tech Stack

### Backend

* Python
* Flask / FastAPI

### AI / NLP

* Sentence Transformers (`all-MiniLM-L6-v2`)

### OCR & Parsing

* Tesseract OCR
* pdfplumber
* BeautifulSoup

### Frontend (Optional)

* Streamlit / React

---

## ⚙️ Installation

```bash
git clone https://github.com/ripudamanss/AI-BASED-NEWSPAPER-SCANNER-.git
cd AI-BASED-NEWSPAPER-SCANNER-

pip install -r requirements.txt
```

---

## ▶️ Usage

### Run the App

```bash
python app.py
```

### Upload

* PDF Newspaper
* OR Image Scan
* OR Paste News Website Link

### Output

* Filtered, categorized UPSC-relevant news
* Downloadable notes

---

## 🧪 Sample AI Logic

```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

syllabus = [
    "Indian Constitution and Polity",
    "Indian Economy and Budget",
    "Environment and Climate Change",
    "International Relations",
    "Science and Technology"
]

def is_relevant(article):
    article_vec = model.encode(article, convert_to_tensor=True)
    syllabus_vec = model.encode(syllabus, convert_to_tensor=True)

    similarity = util.pytorch_cos_sim(article_vec, syllabus_vec)
    return similarity.max() > 0.4
```

---

## 📌 Roadmap

* [ ] Mains Answer Writing Mode
* [ ] PYQ-Based News Linking
* [ ] Mobile App Version
* [ ] Daily Email Digest
* [ ] Voice-Based News Reader
* COMING SOON....
---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your branch (`git checkout -b feature-name`)
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## 💡 Author

**Ripudaman**
B.Tech (AI) | AI Developer

If this project helps you, consider ⭐ starring the repo!

---

## 🏆 Quote

> "Don’t read more. Read what matters."
