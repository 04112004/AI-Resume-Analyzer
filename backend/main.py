from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader
from skills import SKILLS

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# Enable CORS (required for React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

def match_resume(resume_text, job_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_text])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(score * 100, 2)

def feedback(score):
    if score >= 80:
        return "Excellent match"
    elif score >= 60:
        return "Good match"
    else:
        return "Needs improvement"
    
def generate_ai_tips(missing_skills):
    tips = []

    for skill in missing_skills:
        if skill == "fastapi":
            tips.append("Build a REST API project using FastAPI to strengthen backend skills.")
        elif skill == "docker":
            tips.append("Learn Docker basics and containerize one of your projects.")
        elif skill == "aws":
            tips.append("Gain hands-on experience with AWS services like EC2 or S3.")
        elif skill == "sql":
            tips.append("Practice SQL queries and add a database-driven project.")
        else:
            tips.append(f"Add practical experience related to {skill}.")

    return tips

    
def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS if skill in text]


@app.post("/analyze/")
async def analyze_resume(file: UploadFile, job_desc: str = Form(...)):
    resume_text = extract_text_from_pdf(file.file)

    score = match_resume(resume_text, job_desc)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)

    matched_skills = list(set(resume_skills) & set(job_skills))
    missing_skills = list(set(job_skills) - set(resume_skills))

    ai_tips = generate_ai_tips(missing_skills)

    return {
        "score": score,
        "feedback": feedback(score),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "ai_tips": ai_tips
    }

