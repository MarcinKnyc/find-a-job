import streamlit as st
import os
from repositories_qdrant.get_client import get_qdrant_collection_client
from repositories_qdrant.job_offers_pracuj_repository import JobOffersPracujRepository
from langchain.schema import Document
from repositories_postgres.offer_repository import fetch_offer_by_postgres_id
import json
from get_session import get_db_session
job_offers_pracuj_repository = JobOffersPracujRepository()
qdrant_collection_client = get_qdrant_collection_client()
postgres_session = get_db_session()	


st.header("Znajdź najbardziej odpowiednią ofertę pracy do twojego CV!")
sent=st.text_area("Wpisz twoje kwalifikacje i oczekiwania, do 100 słów.", height=400)
# transformed_sent1=cleanInput(sent)
# vector_sent1=vectorizer.transform([transformed_sent1])
# prediction1=model.predict(vector_sent1)[0]

if st.button("Wyszukaj!"):
	found_offers = job_offers_pracuj_repository.similarity_search(
			collection_client=qdrant_collection_client,
			k_approximate_nearest_neighbours=1,
			query=sent,
		)
	found_offer_postgres_id = found_offers[0].metadata[job_offers_pracuj_repository.OFFER_METADATA_POSTGRES_ID_KEY]
	if not found_offer_postgres_id:
		st.success( "Przepraszamy, nie znaleźliśmy odpowiedniej dla Ciebie oferty pracy")
	found_offer = fetch_offer_by_postgres_id(session = postgres_session, offer_postgres_id = found_offer_postgres_id)
	if not found_offer:
		st.success( "Przepraszamy, nie znaleźliśmy odpowiedniej dla Ciebie oferty pracy")
	found_offer_to_pretty_str = job_offers_pracuj_repository.get_offer_description_with_link_str(found_offer)
	st.success(f"Najbardziej odpowiednią dla Ciebie ofertą pracy jest: {found_offer_to_pretty_str}!")

