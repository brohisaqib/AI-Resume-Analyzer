**AI Resume Analyzer & Job Match System**


## 🧠 **Project Overview**

The **AI Resume Analyzer & Job Match System** is a web-based application designed to evaluate resumes and measure their relevance against specific job descriptions. This system integrates **Artificial Intelligence** and **Natural Language Processing (NLP)** techniques to provide detailed insights and recommendations for improving resume quality.

Users can upload their resumes in PDF format and input a job description. The system then analyzes the content, extracts relevant information, and generates a comprehensive report including resume quality, skill gaps, and compatibility with the job role.

---

## ⚙️ **Key Features**

### ✅ Resume Parsing & Text Extraction

* Extracts text from PDF resumes using `pdfplumber`
* Supports scanned documents via OCR (`pytesseract`)

---

### 🤖 AI-Based Resume Analysis

* Utilizes Google Gemini for intelligent evaluation
* Provides:

  * Overall resume score (out of 100)
  * Identified skills
  * Missing or required skills
  * Strengths and weaknesses
  * Actionable improvement suggestions

---

### 📊 Job Match Scoring

* Implements **TF-IDF (Term Frequency–Inverse Document Frequency)** and **Cosine Similarity**
* Calculates how closely a resume matches a given job description
* Outputs a percentage-based compatibility score

---

### 📈 Skills Visualization

* Extracts technical skills from the resume
* Displays results using bar charts for better understanding

---

### 🎯 User-Friendly Interface

* Built using Streamlit
* Clean and interactive layout
* Real-time processing and result display

---

## 🛠️ **Technologies Used**

* **Frontend/UI:** Streamlit
* **AI Integration:** Google Gemini
* **Machine Learning:** TF-IDF, Cosine Similarity
* **Libraries & Tools:**

  * pdfplumber
  * pytesseract (OCR)
  * scikit-learn
  * nltk
  * matplotlib

---

## 🔄 **System Workflow**

1. The user uploads a resume (PDF format)
2. The system extracts textual content from the file
3. The text is cleaned and preprocessed
4. AI model performs resume evaluation
5. Similarity score is computed against the job description
6. Results are displayed, including:

   * Match Score
   * AI-generated feedback
   * Skills visualization

---

## 🎯 **Applications**

* Assists students and job seekers in improving their resumes
* Helps in creating ATS-friendly resumes
* Supports recruiters in preliminary resume screening

---

## 🚀 **Future Enhancements**

* Downloadable PDF reports
* Multi-job comparison feature
* Advanced NLP-based skill extraction
* User authentication system
* Integration with job portals for live recommendations

---

## ⚡ **Short Summary**

This project leverages AI and machine learning techniques to analyze resumes and evaluate their alignment with job descriptions. It provides users with actionable insights, match scores, and recommendations to enhance their employability.

