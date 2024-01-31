import html
from flask import Flask, request, jsonify
import os
from repositories_qdrant.get_client import get_qdrant_collection_client
from repositories_qdrant.job_offers_pracuj_repository import JobOffersPracujRepository
from langchain.schema import Document
from repositories_postgres.offer_repository import fetch_offer_by_postgres_id
import json
from get_session import get_db_session


app = Flask(__name__)
job_offers_pracuj_repository = JobOffersPracujRepository()
qdrant_collection_client = get_qdrant_collection_client()
postgres_session = get_db_session()

@app.route('/job_search',methods = ['POST'])
def sentimentCheck():
	if request.method == 'POST':
		request_json = request.json
		text = request_json['text']
		number_of_offers = request_json['number_of_offers'] if 'number_of_offers' in request_json.keys() else 10 # default value
		found_offers = job_offers_pracuj_repository.similarity_search(
			collection_client=qdrant_collection_client,
			k_approximate_nearest_neighbours=number_of_offers,
			query=text,
		)
		if len(found_offers) == 0 or not found_offers[0].metadata[job_offers_pracuj_repository.OFFER_METADATA_POSTGRES_ID_KEY]:
			# should never happen, is just error detection (unless the database is empty :) )
			return "Przykro nam, nie znaleźliśmy odpowiedniej dla Ciebie oferty pracy."
		offers_exported = []
		for offer in found_offers:
			found_offer_postgres_id = offer.metadata[job_offers_pracuj_repository.OFFER_METADATA_POSTGRES_ID_KEY]
			found_offer = fetch_offer_by_postgres_id(session = postgres_session, offer_postgres_id = found_offer_postgres_id)
			if not found_offer:
				# should never happen; is just error handling here
				continue
			found_offer_to_pretty_str = job_offers_pracuj_repository.get_offer_description_with_link_str(found_offer)			
			offers_exported.append(found_offer_to_pretty_str)
		return offers_exported


if __name__ == "__main__":
    port = int(os.environ.get("JOB_REST_PORT", 15000))
    app.run(debug=True,host='0.0.0.0',port=port)

