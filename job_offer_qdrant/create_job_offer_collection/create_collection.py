from qdrant_client import QdrantClient, models
import json


def recreate_collection(config_filename: str) -> None:
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
    config = json.load(open(f'configs/{config_filename}'))
    api_key = config['api_key']
    port = config['port']
    host = config['host']
    collection_name = config['collection_name']
    model_vector_size = config['model_vector_size']
    on_disk = config['on_disk']
    client = QdrantClient(
        host=host,
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
    recreate_collection('default.json')