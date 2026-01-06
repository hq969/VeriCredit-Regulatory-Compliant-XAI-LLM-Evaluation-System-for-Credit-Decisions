from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def human_ai_agreement(human_text, llm_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([human_text, llm_text])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(similarity, 2)
