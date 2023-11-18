from typing import List
from langchain.vectorstores.qdrant import Qdrant
from langchain.schema import Document
from models import Offer


class JobOffersPracujRepository:
    OFFER_METADATA_POSTGRES_ID_KEY = "offer_postgres_id"
    def similarity_search(
        self,
        query: str,
        collection_client: Qdrant,
        k_approximate_nearest_neighbours: int,
    ) -> List[Document]:
        """Extract text from langchain.schema.Document by Document.page_content"""
        return collection_client.similarity_search(
            query=query, k=k_approximate_nearest_neighbours
        )

    def add_documents(
        self, pracuj_job_descriptions: List[Offer], collection_client: Qdrant
    ) -> None:
        collection_client.add_documents(
            documents=[
                Document(
                    page_content=self.get_offer_description_str(job_offer=job_offer),
                    metadata={self.OFFER_METADATA_POSTGRES_ID_KEY: job_offer.id},
                )
                for job_offer in pracuj_job_descriptions
            ],
        )

    def get_offer_description_str(self, job_offer: Offer) -> str:
        result = f"{job_offer.title}\n\nObowiązki: {job_offer.responsibilities}\n\n"
        if job_offer.experience_requirements:
            result += f"Wymagania: {job_offer.experience_requirements}\n\n"
        result += f"Branża: {job_offer.industry}\n\Typ zatrudnienia: {job_offer.employment_type}\n\n"
        if job_offer.job_benefits:
            result += f"Benefity: {job_offer.job_benefits}\n\n"
        return result
