from qdrant_client import QdrantClient, models
import os


def recreate_collection() -> None:
    """
    IMPORTANT!
    The config files don't contain the secret API key. 
    You need to modify the config and paste the API key in plain text :D
    Arguments:
    config_filename: config filename without path
    Returns: 
    UserWarning: Api key is used with unsecure connection.
    warnings.warn("Api key is used with unsecure connection.") 
    xD
    """
    api_key = os.environ['JOB_API_KEY']
    port = os.environ['JOB_PORT']
    host = os.environ['JOB_HOST']
    collection_name = os.environ['JOB_COLLECTION_NAME']
    model_vector_size = os.environ['JOB_MODEL_VECTOR_SIZE']
    on_disk = os.environ['JOB_ON_DISK']
    client = QdrantClient(
        url=host,
        port=port,
        api_key=api_key
        )

    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(size=model_vector_size, distance=models.Distance.COSINE),
        optimizers_config=models.OptimizersConfigDiff(memmap_threshold=20000),
        hnsw_config=models.HnswConfigDiff(on_disk=on_disk)
    )

if __name__ == '__main__':
    recreate_collection()