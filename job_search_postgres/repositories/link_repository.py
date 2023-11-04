from models import Link
from sqlalchemy.orm.session import Session

def fetch_all_links(session: Session) -> list[Link]:
    return session.query(Link).all()