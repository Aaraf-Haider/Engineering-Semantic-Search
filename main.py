from document_manager import add_document , view_documents
from embedding_service import generate_embeddings , clear_embeddings
from similarity import compare_sentences
from search_engine import semantic_search

def display_menu():
    print("="*40)
    print("ENGINEERING SEMANTIC SEARCH ENGINE")
    print("="*40)
    print("\n")
    print("1.  Add Document ")
    print("2.  Generate Document Embedding")
    print("3.  Semantic Search ")
    print("4.  Compare Two Sentences ")
    print("5.  View All Documents ")
    print("6.  Clear Embeddings ")
    print("7.  Exit")


def main():

    while True:
        display_menu()
        choice = input("Choose any option: ").strip()
        if choice == "1":
            add_document()
        elif choice == "2":
            generate_embeddings()
        elif choice == "3":
            semantic_search()
        elif choice == "4":
            compare_sentences()
        elif choice == "5":
            view_documents()
        elif choice == "6":
            clear_embeddings()
        elif choice == "7":
            print("Exiting Application")
            break
        else:
            print("Invalid choice. choose between 1 to 7")
            
if __name__ == "__main__":
    main()