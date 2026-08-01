"""
vector_store.py
----------------
STEP 3 of the pipeline:
  - Reads the pickle file of face encodings (dataset/encodings.pkl)
  - Pushes each encoding vector into a ChromaDB collection, so we can do
    fast nearest-neighbour vector search during live attendance.

Run this once whenever new students are enrolled or re-enrolled:
    python vector_store.py
"""

import pickle
import os
import chromadb

ENCODINGS_FILE = "encodings/encodings.pkl"
CHROMA_DB_PATH = "chroma_db"          # local persistent folder for the vector DB
COLLECTION_NAME = "student_faces"


def load_pickle_encodings():
    if not os.path.exists(ENCODINGS_FILE):
        raise FileNotFoundError(
            f"{ENCODINGS_FILE} not found. Run enroll.py first to generate encodings."
        )
    with open(ENCODINGS_FILE, "rb") as f:
        return pickle.load(f)


def build_vector_store():
    data = load_pickle_encodings()

    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

    # Fresh collection each time we rebuild, so stale/old students don't linger
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "l2"}  # Euclidean distance, matches face_recognition's compare_faces logic
    )

    ids, embeddings, metadatas = [], [], []

    for name, info in data.items():
        roll_no = info["roll_no"]
        for i, enc in enumerate(info["encodings"]):
            ids.append(f"{name}_{roll_no}_{i}")
            embeddings.append(enc.tolist())
            metadatas.append({"name": name, "roll_no": roll_no})

    if not ids:
        print("[WARN] No encodings found to insert.")
        return

    collection.add(ids=ids, embeddings=embeddings, metadatas=metadatas)
    print(f"[SUCCESS] Inserted {len(ids)} face vectors into ChromaDB collection '{COLLECTION_NAME}'.")
    print(f"[INFO] Students indexed: {list(data.keys())}")


def get_collection():
    """Helper used by attendance.py to fetch the existing collection."""
    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    return client.get_collection(COLLECTION_NAME)


if __name__ == "__main__":
    build_vector_store()
