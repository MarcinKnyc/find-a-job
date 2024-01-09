from models import Link, Offer
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import func


def fetch_all_offers(session: Session) -> list[Offer]:
    return session.query(Offer).all()

def fetch_n_random_offers(session: Session, n_offers: int) -> list[Offer]:
    return (
        session.query(Offer)
        .order_by(func.random())
        .limit(n_offers)
        .all()
    )

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

def fetch_offer_by_link(session: Session, offer_link: str) -> Offer:
    return (
        session
        .query(Offer)
        .join(Offer.link)
        .filter(Link.link == offer_link)
        .first()
    )

def insert_offer(offer: Offer, session: Session) -> None:
    session.add(offer)
    session.commit()
