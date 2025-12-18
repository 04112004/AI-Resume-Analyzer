from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from skills import SKILLS

app = FastAPI()

# -------------------- CORS (Required for React) --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for demo / portfolio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- PDF TEXT EXTRACTION --------------------
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text.lower()

# -------------------- SKILL EXTRACTION --------------------
def extract_skills(text):
    return [skill for skill in SKILLS if skill in text]

# -------------------- ATS SCORING (SKILLS + TEXT SIMILARITY) --------------------
def calculate_ats_score(resume_text, job_text, matched_skills, job_skills):
    # ---------- Text similarity (TF-IDF) ----------
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_text])
    text_similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    text_score = text_similarity * 100

    # ---------- Skill match score ----------
    total_skills = len(job_skills)
    matched_count = len(matched_skills)

    if total_skills == 0:
        skill_score = 0
    else:
        skill_score = (matched_count / total_skills) * 100

    # ---------- Final weighted ATS score ----------
    # 70% skills + 30% text relevance
    final_score = (0.7 * skill_score) + (0.3 * text_score)

    return round(final_score, 2)

# -------------------- FEEDBACK BASED ON SCORE --------------------
def generate_feedback(score):
    if score >= 85:
        return "Excellent match"
    elif score >= 65:
        return "Good match"
    elif score >= 45:
        return "Average match"
    else:
        return "Needs improvement"

# -------------------- AI IMPROVEMENT TIPS --------------------
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

# -------------------- MAIN ANALYZE ENDPOINT --------------------
@app.post("/analyze/")
async def analyze_resume(
    file: UploadFile = File(...),
    job_desc: str = Form(...)
):
    # Extract text
    resume_text = extract_text_from_pdf(file.file)
    job_text = job_desc.lower()

    # Extract skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    matched_skills = list(set(resume_skills) & set(job_skills))
    missing_skills = list(set(job_skills) - set(resume_skills))

    # Calculate ATS score
    score = calculate_ats_score(
        resume_text,
        job_text,
        matched_skills,
        job_skills
    )

    # Feedback & tips
    feedback = generate_feedback(score)
    ai_tips = generate_ai_tips(missing_skills)

    return {
        "score": score,
        "feedback": feedback,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "ai_tips": ai_tips
    }
