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


st.header("Znajdź najbardziej odpowiednie oferty pracy do twojego CV!")
sent=st.text_area("Wpisz twoje kwalifikacje i oczekiwania, do 200 słów.", height=400)
number_of_offers = st.number_input(
	label="Ile ofert pracy chcesz wyświetlić?", 
	min_value=1, 
	max_value=50, 
	value=5,
)
# transformed_sent1=cleanInput(sent)
# vector_sent1=vectorizer.transform([transformed_sent1])
# prediction1=model.predict(vector_sent1)[0]

if st.button("Wyszukaj!"):
	found_offers = job_offers_pracuj_repository.similarity_search(
			collection_client=qdrant_collection_client,
			k_approximate_nearest_neighbours=number_of_offers,
			query=sent,
		)
	if len(found_offers) == 0 or not found_offers[0].metadata[job_offers_pracuj_repository.OFFER_METADATA_POSTGRES_ID_KEY]:
		# should never happen, is just error detection
		st.error( "Przepraszamy, nie znaleźliśmy odpowiedniej dla Ciebie oferty pracy")
	else:
		to_print = ""
		for offer in found_offers:
			found_offer_postgres_id = offer.metadata[job_offers_pracuj_repository.OFFER_METADATA_POSTGRES_ID_KEY]		
			found_offer = fetch_offer_by_postgres_id(session = postgres_session, offer_postgres_id = found_offer_postgres_id)
			if not found_offer:
				# should never happen; is just error handling here
				continue
			found_offer_to_pretty_str = job_offers_pracuj_repository.get_shortened_offer_description_with_link_str(
				job_offer=found_offer, character_limit=410
			)
			to_print += found_offer_to_pretty_str
			to_print += "------------------------------------- \n\n"
		
		if not to_print: 
			st.error( "Przepraszamy, nie znaleźliśmy odpowiedniej dla Ciebie oferty pracy")
		st.success(f"Najbardziej odpowiednimi dla Ciebie ofertami pracy są: \n\n{to_print}")

