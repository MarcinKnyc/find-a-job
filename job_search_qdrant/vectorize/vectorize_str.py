from sentence_transformers import SentenceTransformer

def vectorize_long_string(model: any, string_to_vectorize: str) -> list[float]:
    embeddings = model.encode([string_to_vectorize])
    return embeddings[0]

def get_model(model_name: str) -> any:
    model = SentenceTransformer(model_name)
    return model

