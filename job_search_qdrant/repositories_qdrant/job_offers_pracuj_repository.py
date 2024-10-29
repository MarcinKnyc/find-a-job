from typing import List
from langchain_community.vectorstores import Qdrant
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
        """
        Vectorize and store job offer descriptions in Qdrant. Connection details should be in environment variables.
        Careful! This function WILL insert duplicate vectors if you let it. Avoiding duplicate vectors in qdrant should be handled by 
            exported_to_qdrant field of model Offer in postgres.
        """
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
        result += f"Branża: {job_offer.industry}\n\nTyp zatrudnienia: {job_offer.employment_type}\n\n"
        if job_offer.job_benefits:
            result += f"Benefity: {job_offer.job_benefits}\n\n"
        return result

    def get_offer_description_with_link_str(self, job_offer: Offer) -> str:
        result = f"Link: {job_offer.link.link}\n\n"
        result += f"{job_offer.title}\n\nObowiązki: {job_offer.responsibilities}\n\n"
        if job_offer.experience_requirements:
            result += f"Wymagania: {job_offer.experience_requirements}\n\n"
        result += f"Branża: {job_offer.industry}\n\nTyp zatrudnienia: {job_offer.employment_type}\n\n"
        if job_offer.job_benefits:
            result += f"Benefity: {job_offer.job_benefits}\n\n"
        return result
    
    def get_shortened_offer_description_with_link_str(self, job_offer: Offer, character_limit: int = 230) -> str:        
        result = f"{job_offer.title} - {job_offer.hiring_organization} \n\n"
        result += f"{job_offer.link.link} \n\n"
        result += f"{job_offer.responsibilities} \n\n"
        if job_offer.experience_requirements:
            result += f"Wymagania: {job_offer.experience_requirements} \n\n"
        result += f"Branża: {job_offer.industry} \n\n Typ zatrudnienia: {job_offer.employment_type} \n\n"
        if job_offer.job_benefits:
            result += f"Benefity: {job_offer.job_benefits} \n\n"
        return result[:character_limit] + "... \n\n"
    