from sentence_transformers import SentenceTransformer
import numpy as np
from config import MODEL_NAME , EMBEDDINGS_PATH
from document_manager import load_documents
def get_model():
    model = SentenceTransformer(MODEL_NAME)
    return model

def generate_embeddings():
    documents = load_documents()
    if not documents:
        print("No documents exist")
        return
    texts = [document['text'] for document in documents]
    model = get_model()
    embedding = model.encode(texts)
    print(embedding.shape)
    np.save(EMBEDDINGS_PATH , embedding)
    print("Embedding saved successfully")

def load_embeddings():
    if EMBEDDINGS_PATH.exists():
        embedding = np.load(EMBEDDINGS_PATH)
        return embedding
    print("Embedding doesn't exist")
    return None

def clear_embeddings():
    if not EMBEDDINGS_PATH.exists():
        print("No embedding files here")
        return
    EMBEDDINGS_PATH.unlink()
    print("Embedding cleared successfully")