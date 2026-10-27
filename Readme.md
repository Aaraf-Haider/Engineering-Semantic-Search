# Engineering Semantic Search Engine

A modular, command-line semantic search application built with Python, Sentence Transformers, and NumPy. It stores documents as JSON, creates local embedding vectors, and retrieves relevant documents using cosine similarity.

## Features

1. **Add Document** — Enter text manually or import a UTF-8 `.txt` file. Each document receives a UUID and includes a title and category.
2. **Generate Document Embeddings** — Encode all saved document texts using `sentence-transformers/all-MiniLM-L6-v2` and save the vectors locally.
3. **Semantic Search** — Compare a natural-language query against stored embeddings, rank matches by cosine similarity, apply a threshold, and display Top-K results.
4. **Compare Two Sentences** — Generate sentence embeddings and compute their cosine similarity.
5. **View All Documents** — List saved document IDs, titles, and categories.
6. **Clear Embeddings** — Remove generated vectors while preserving document data.
7. **Exit** — Close the application.

## Project structure

```text
engineering_semantic_search/
├── main.py
├── config.py
├── document_manager.py
├── embedding_service.py
├── similarity.py
├── search_engine.py
├── requirements.txt
├── .gitignore
└── data/
    ├── documents.json
    └── embeddings.npy  # generated locally; not committed
```

## Installation

Requires Python 3.10+ (use a version supported by your installed PyTorch and Sentence Transformers packages).

```bash
git clone https://github.com/YOUR_USERNAME/engineering_semantic_search.git
cd engineering_semantic_search
python -m venv venv
```

Activate your environment:

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

First add or review the sample documents, then choose **2. Generate Document Embeddings** before using **3. Semantic Search**. New documents invalidate existing embeddings, so generate them again after adding a document.

Example search question:

```text
Which programming language is used for artificial intelligence?
```

The search engine displays matching document titles with cosine similarity scores. Results depend on the document content, model, and configured threshold.

## Configuration

Edit `config.py` to adjust:

- `MODEL_NAME`: Sentence Transformer model (default: `sentence-transformers/all-MiniLM-L6-v2`)
- `TOP_K`: Maximum number of results to display (default: `3`)
- `THRESHOLD`: Minimum cosine similarity score (default: `0.50`)
- `DOCUMENTS_PATH` and `EMBEDDINGS_PATH`: Local data file locations

Changing the embedding model requires regenerating document embeddings.

## How semantic search works

1. Load the document collection from `data/documents.json`.
2. Generate and save a vector for each document in matching order.
3. Encode the user's query with the same model.
4. Calculate cosine similarity between the query vector and each document vector.
5. Sort scores descending, filter by the configured threshold, and show up to `TOP_K` matches.

## Notes

- The model may download weights on first use; an internet connection may be needed initially.
- The `.npy` file is generated data and is ignored by Git.
- This is a local learning project; it does not require an external vector database.
- Before publishing documents, make sure they don't contain sensitive or proprietary material.

## Technology

Python · Sentence Transformers · NumPy · JSON · Git
