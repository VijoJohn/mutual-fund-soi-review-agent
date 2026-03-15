import os
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()

collection = client.create_collection("soi_knowledge")


def load_knowledge():

    base_path = "knowledge"

    documents = []

    for root, dirs, files in os.walk(base_path):

        for file in files:

            path = os.path.join(root, file)

            with open(path, "r") as f:
                text = f.read()

            documents.append(text)

    for i, doc in enumerate(documents):

        embedding = model.encode(doc).tolist()

        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[doc]
        )


def retrieve_context(query):

    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    return results["documents"][0]
