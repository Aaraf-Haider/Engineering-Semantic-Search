import json
from config import DOCUMENTS_PATH , EMBEDDINGS_PATH
import uuid
from pathlib import Path

def load_documents():
    if DOCUMENTS_PATH.exists():
        with open(DOCUMENTS_PATH , 'r' , encoding='utf-8') as f:
            documents = json.load(f)
        return documents
    else:
        return []

def save_documents(documents):
    with open(DOCUMENTS_PATH , 'w' , encoding='utf-8') as f:
        json.dump(documents, f , indent = 4)

def add_document():
    documents = load_documents()
    document_id = str(uuid.uuid4())
    title = input("Enter a document title: ").strip()
    while not title:
        print("Invalid Title")
        title = input("Enter a document title: ").strip()
    
    category = input("Enter a document category: ").strip()
    while not category:
        print("Invalid category")
        category = input("Enter a document category: ").strip()

    print("1. Enter Text Manually")
    print("2. Enter .txt File")
    choice = input("Choose one number: ").strip()
    if choice == '1':
        text = input("Enter a document text: ").strip()
        while not text:
            print("Invalid Text")
            text = input("Enter a document text: ").strip()
    elif choice == '2':
        text = read_txt_file()
        if not text:
            print("Invalid Text")
            return
    else:
        print("Invalid Choice")
        return
    new_document = { "id" : document_id , "title" : title , "category" : category , "text" : text}
    documents.append(new_document)
    save_documents(documents)
    print("Document added  successfully")
    if EMBEDDINGS_PATH.exists():
        EMBEDDINGS_PATH.unlink()
        print("Embedding outdated please regenerate it")

def read_txt_file():
    file_path = input("Enter txt file path: ").strip()
    while not file_path:
        print("Invaliid File path")
        file_path = input("Enter txt file path: ").strip()
    file = Path(file_path).resolve()
    if file.is_file() and file.suffix.lower() == ".txt":
        with open(file , 'r' , encoding = 'utf-8') as f:
            text = f.read().strip()
            return text
    else:
        print("File not found or invalid file type. Only .txt files are allowed.")
        return None

def view_documents():
    documents = load_documents()
    if not documents:
        print("No document available")
        return
    else:
        print("Total Number of Document: " , len(documents))
        for number , document in enumerate(documents , start = 1):
            print(f"No. {number}")
            print(f"ID: {document['id']}")
            print(f"Title: {document['title']}")
            print(f"Cateogry: {document['category']}")
            print("\n ***************** \n")