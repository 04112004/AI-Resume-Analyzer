# AI Resume Analyzer 🚀

An AI-powered Resume Analyzer that evaluates a candidate’s resume against a given job description and provides an ATS-style score, matched skills, missing skills, and improvement feedback.

This project simulates how Applicant Tracking Systems (ATS) work in real-world recruitment.

---

## 🔥 Features

- Upload resume in PDF format
- Paste any job description
- ATS-style resume match score
- Skill matching (matched & missing skills)
- AI-generated feedback
- Clean, modern UI with dark theme
- FastAPI backend with REST API
- React + Vite frontend

---

## 🛠️ Tech Stack

### Frontend
- React
- Vite
- JavaScript
- CSS (custom styling)

### Backend
- FastAPI
- Python
- NLP (TF-IDF, Cosine Similarity)
- Uvicorn

---

## 🧠 How It Works

1. Resume PDF is uploaded by the user
2. Text is extracted from the resume
3. Job description text is processed
4. NLP techniques calculate similarity score
5. Skills are matched between resume & job description
6. Missing skills and improvement feedback are generated

---

## 📂 Project Structure

AI-Resume-Analyzer/
│
├── frontend/ # React frontend
├── backend/ # FastAPI backend
├── README.md
└── .gitignore

## Backend setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload


Backend will run at:

http://127.0.0.1:8000

## Frontend setup
cd frontend
npm install
npm run dev


Frontend will run at:

http://localhost:5173

## 🚀 Live Demo
🔗 https://ai-resume-analyzer-nine-blush.vercel.app


