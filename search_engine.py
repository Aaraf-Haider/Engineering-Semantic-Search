from document_manager import load_documents
from embedding_service import load_embeddings , get_model
from similarity import cosine_similarity
from config import TOP_K , THRESHOLD

def semantic_search():

    documents = load_documents()
    if not documents:
        print("no document found")
        return
    embeddings = load_embeddings()
    if embeddings is None:
        print("no embedding found return")
        return
    if len(documents) != len(embeddings):
        print("please regenerate embeddings")
        return
    
    print(f"Total number of documents and embeddings: {len(documents)} & {embeddings.shape}")

    
    query = input("Enter a search query").strip()
    if not query:
        print("invalid query")
        return
    model = get_model()
    query_embedding = model.encode(query)
    print("query embedding shape" , query_embedding.shape)

    results = []
    for document , embedding in zip(documents , embeddings):
        score = cosine_similarity(query_embedding , embedding)
        results.append((document , score))

    ranking = sorted(results , key= lambda x:x[1] , reverse = True) 
    
    filtered_results = [scor for scor in ranking if scor[1] >= THRESHOLD ]

    top_results = filtered_results[:TOP_K]

    if not top_results:
        print("No Relevant Document")
        return
    
    for document , score in top_results:
        print(f"Title: {document['title']}")
        print(f"Similarity Score: {score:.4f}")
        print("-"*40)

