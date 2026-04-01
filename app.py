import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import pdfplumber
from pdf2image import convert_from_path
import pytesseract
import matplotlib.pyplot as plt
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ------------------- SETUP -------------------
st.set_page_config(page_title="AI Resume Analyzer Pro", layout="wide")

load_dotenv()
#genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Download NLTK
@st.cache_data
def download_nltk():
    nltk.download('stopwords', quiet=True)

download_nltk()

# ------------------- PDF TEXT EXTRACTION -------------------
def extract_text_from_pdf(pdf_path):
    text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text += t
    except:
        pass

    # OCR fallback
    if not text.strip():
        try:
            images = convert_from_path(pdf_path)
            for img in images:
                text += pytesseract.image_to_string(img)
        except:
            pass

    return text.strip()

# ------------------- AI ANALYSIS -------------------
def analyze_resume(resume_text):
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    Analyze resume and give:
    - Score (100)
    - Skills
    - Missing Skills
    - Strengths
    - Weaknesses
    - Improvements

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)
    return response.text if response else "No response"

# ------------------- CLEAN TEXT -------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    return " ".join([w for w in text.split() if w not in stop_words])

# ------------------- MATCH SCORE -------------------
def calculate_similarity(resume, job):
    r = remove_stopwords(clean_text(resume))
    j = remove_stopwords(clean_text(job))

    tfidf = TfidfVectorizer()
    vec = tfidf.fit_transform([r, j])

    score = cosine_similarity(vec[0:1], vec[1:2])[0][0] * 100
    return round(score, 2)

# ------------------- SKILLS -------------------
def extract_skills(text):
    skills = ["python","sql","machine learning","excel","html","css","javascript","pandas"]
    found = []

    for s in skills:
        if s in text.lower():
            found.append(s)

    return found

def plot_chart(skills):
    c = Counter(skills)
    plt.figure(figsize=(8,3))
    plt.bar(c.keys(), c.values())
    plt.xticks(rotation=45)
    st.pyplot(plt)

# ------------------- UI -------------------
st.title("🚀 AI Resume Analyzer + Job Match")

col1, col2 = st.columns(2)

with col1:
    file = st.file_uploader("Upload Resume PDF", type=["pdf"])

with col2:
    job_desc = st.text_area("Paste Job Description")

# ------------------- PROCESS -------------------
if st.button("🔥 Analyze Complete"):

    if not file or not job_desc:
        st.warning("Upload resume + add job description")
        st.stop()

    with open("temp.pdf","wb") as f:
        f.write(file.getbuffer())

    with st.spinner("Processing..."):
        text = extract_text_from_pdf("temp.pdf")

        # AI Analysis
        ai_result = analyze_resume(text)

        # Match Score
        score = calculate_similarity(text, job_desc)

        # Skills
        skills = extract_skills(text)

    # ------------------- OUTPUT -------------------

    st.success("Done ✅")

    # Match Score
    st.subheader("📊 Match Score")
    st.metric("Score", f"{score}%")

    # Chart
    fig, ax = plt.subplots(figsize=(8,1))
    ax.barh([""], [score])
    ax.set_xlim(0,100)
    ax.set_title("Match Level")
    st.pyplot(fig)

    # AI Analysis
    st.subheader("🤖 AI Resume Analysis")
    st.write(ai_result)

    # Skills
    if skills:
        st.subheader("📈 Skills Chart")
        plot_chart(skills)
    else:
        st.warning("No skills found")

# ------------------- FOOTER -------------------
st.markdown("---")
st.markdown("Made by Saqib Brohi")
