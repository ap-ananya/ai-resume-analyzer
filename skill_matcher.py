from sklearn.feature_extraction.text import TfidfVectorizer

def extract_skills(text, top_n=15):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=top_n)
    vectorizer.fit([text])
    return vectorizer.get_feature_names_out()

def compare_skills(resume_skills, jd_skills):
    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched = list(resume_set.intersection(jd_set))
    missing = list(jd_set - resume_set)

    return matched, missing

def generate_suggestions(score, missing_skills):
    suggestions = []

    if score < 50:
        suggestions.append("Resume has low alignment. Consider restructuring your resume.")

    if missing_skills:
        suggestions.append("Add projects or experience related to missing skills.")

    suggestions.append("Use measurable achievements and action verbs.")

    return suggestions

def extract_ats_keywords(text, top_n=20):
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=top_n
    )
    vectorizer.fit([text])
    return list(vectorizer.get_feature_names_out())


def ats_missing_keywords(resume_text, jd_text):
    jd_keywords = set(extract_ats_keywords(jd_text))
    resume_keywords = set(extract_ats_keywords(resume_text))

    missing = list(jd_keywords - resume_keywords)
    return missing
