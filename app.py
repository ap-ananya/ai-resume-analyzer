from flask import Flask, render_template, request
from resume_parser import extract_text, extract_sections
from similarity import calculate_similarity, section_similarity
from skill_matcher import (
    extract_skills,
    compare_skills,
    generate_suggestions,
    ats_missing_keywords
)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    resume_file = request.files['resume']
    job_description = request.form['job_description']

    resume_text = extract_text(resume_file)
    ats_keywords = ats_missing_keywords(resume_text, job_description)


    resume_sections = extract_sections(resume_text)
    section_scores = section_similarity(resume_sections, job_description)


    score = calculate_similarity(resume_text, job_description)

    jd_skills = extract_skills(job_description)
    resume_skills = extract_skills(resume_text)

    matched, missing = compare_skills(resume_skills, jd_skills)
    suggestions = generate_suggestions(score, missing)

    return render_template(
        "index.html",
        score=score,
        matched_skills=matched,
        missing_skills=missing,
        suggestions=suggestions,
        section_scores=section_scores,
        ats_keywords=ats_keywords
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
