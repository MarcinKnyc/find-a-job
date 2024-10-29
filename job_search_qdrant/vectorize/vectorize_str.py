from sentence_transformers import SentenceTransformer

from get_session import get_db_session
from models import Offer
from repositories_qdrant.job_offers_pracuj_repository import JobOffersPracujRepository

def vectorize_long_string(model: any, string_to_vectorize: str) -> list[float]:
    """
    Functions in this file are never used in the project. 
        They were written only for the purpose of visualising the process of sentence embedding.
    """
    embeddings = model.encode([string_to_vectorize])
    return embeddings[0].tolist()

def get_model(model_name: str) -> any:
    model = SentenceTransformer(model_name)
    return model

if __name__ == '__main__':
    model = get_model('sdadas/st-polish-paraphrase-from-distilroberta')
    session = get_db_session() # need env vars
    offer = session.query(Offer).filter(Offer.title == 'Opiekun Klienta Farmaceutycznego').one()
    repo = JobOffersPracujRepository()
    print(repo.get_offer_description_str(offer))
    print(vectorize_long_string(model, 'Mam doświadczenie w sprzedaży sprzętu medycznego. Jestem zorientowany w ofercie najlepszych firm farmaceutycznych oraz mam doświadczenie w nawiązywaniu stałych, długotrwałych kontaktów z lekarzami. Ukończyłem studia, mam samochód oraz prawo jazdy kat. B.')) # zapytanie
    print(vectorize_long_string(model, repo.get_offer_description_str(offer))) # opis jakiejś oferty