from models import Offer
from sqlalchemy.orm.session import Session


def fetch_all_offers(session: Session) -> list[Offer]:
    return session.query(Offer).all()


def fetch_all_offers_not_exported_to_qdrant(session: Session) -> list[Offer]:
    return (
        session
        .query(Offer)
        .filter(Offer.exported_to_qdrant == None)
        .all()
    )

def fetch_offer_by_postgres_id(session: Session, offer_postgres_id: int) -> Offer:
    return (
        session
        .query(Offer)
        .filter(Offer.id == offer_postgres_id)
        .one()
    )

def insert_offer(offer: Offer, session: Session) -> None:
    session.add(offer)
    session.commit()
