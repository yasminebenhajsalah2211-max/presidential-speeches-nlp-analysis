from sklearn.feature_extraction.text import TfidfVectorizer

def compute_tfidf(texts):

    vectorizer = TfidfVectorizer(max_features=1000)

    tfidf_matrix = vectorizer.fit_transform(texts)

    return tfidf_matrix, vectorizer