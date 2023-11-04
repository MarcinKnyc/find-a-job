from models import Offer
from sqlalchemy.orm.session import Session


def fetch_all_offers(session: Session) -> list[Offer]:
    return session.query(Offer).all()


def insert_offer(offer: Offer, session: Session) -> None:
    session.add(offer)
    session.commit()
