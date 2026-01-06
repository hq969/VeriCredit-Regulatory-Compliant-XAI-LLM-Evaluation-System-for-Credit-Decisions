from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def explanation_drift(baseline, current):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([baseline, current])
    similarity = cosine_similarity(vectors)[0][1]
    return round(1 - similarity, 2)
