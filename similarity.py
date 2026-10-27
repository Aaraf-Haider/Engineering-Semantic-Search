import numpy as np
from embedding_service import get_model

def cosine_similarity(vector_a , vector_b):
    dot_product = np.dot(vector_a , vector_b)
    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
    similarity_score = dot_product / (magnitude_a * magnitude_b)
    return similarity_score

def compare_sentences():
    sentence1 = input("Enter 1st Sentence: ").strip()
    sentence2 = input("\nEnter 2nd Sentence: ").strip()
    if not sentence1 or not sentence2:
        print("empty sentence")
        return
    model = get_model()
    embedding1 = model.encode(sentence1)
    embedding2 = model.encode(sentence2)
    similarity = cosine_similarity(embedding1 , embedding2)
    print(f"Similarity Score: {similarity:.2f}")