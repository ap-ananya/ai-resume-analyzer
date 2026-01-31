from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import clean_text


def calculate_similarity(text1, text2):
    text1 = clean_text(text1)
    text2 = clean_text(text2)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])

    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(score * 100, 2)


def section_similarity(resume_sections, jd_text):
    scores = {}

    for section, content in resume_sections.items():
        if content.strip():
            scores[section] = calculate_similarity(content, jd_text)
        else:
            scores[section] = 0.0

    return scores
