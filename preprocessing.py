import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)

    words = text.split()
    stop_words = set(stopwords.words('english'))

    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]

    return " ".join(words)
