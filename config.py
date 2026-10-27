from pathlib import Path

PROJECT_FOLDER = Path(__file__).resolve().parent
DATA_FOLDER = PROJECT_FOLDER / "data"
DATA_FOLDER.mkdir(parents= True , exist_ok=True)
DOCUMENTS_PATH = DATA_FOLDER / "documents.json"
EMBEDDINGS_PATH = DATA_FOLDER / "embeddings.npy"

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K = 3
THRESHOLD = 0.50