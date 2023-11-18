import os
import qdrant_client
from langchain.vectorstores import qdrant
from langchain.embeddings import HuggingFaceEmbeddings

def get_qdrant_collection_client():
    api_key = os.environ['JOB_API_KEY']
    port = os.environ['JOB_PORT']
    host = os.environ['JOB_HOST']
    collection_name = os.environ['JOB_COLLECTION_NAME']
    model_name = os.environ['JOB_MODEL_NAME']
    

    embeddings = HuggingFaceEmbeddings(
        model_name=model_name
    )

    qdrant_url = f"{host}:{port}"
    client = qdrant_client.QdrantClient(
        qdrant_url,
        api_key=api_key, # For Qdrant Cloud, None for local instance
    )

    doc_store = qdrant.Qdrant(
        client=client, collection_name=collection_name, 
        embeddings=embeddings,
    )

    return doc_store
