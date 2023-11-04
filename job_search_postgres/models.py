from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Link(Base):
    __tablename__ = 'links'
    __table_args__ = {'schema': 'links'}

    id = Column(Integer, primary_key=True)
    link = Column(Text, nullable=False, unique=True)
    date_added = Column(DateTime, nullable=False)

    offers = relationship("Offer", back_populates="link")


class Offer(Base):
    __tablename__ = 'offers'
    __table_args__ = {'schema': 'offers'}

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    hiring_organization = Column(Text, nullable=False)
    date_posted = Column(DateTime, nullable=False)
    valid_through = Column(DateTime, nullable=False)
    address_country = Column(Text, nullable=False)
    address_region = Column(Text, nullable=False)
    address_locality = Column(Text)
    postal_code = Column(Text)
    street_address = Column(Text)
    employment_type = Column(Text, nullable=False)
    industry = Column(Text, nullable=False)
    base_salary_min = Column(Float)
    base_salary_max = Column(Float)
    base_salary_currency = Column(Text)
    base_salary_unit = Column(Text)
    job_benefits = Column(Text)
    responsibilities = Column(Text, nullable=False)
    experience_requirements = Column(Text)
    link_id = Column(Integer, ForeignKey('links.links.id'))

    link = relationship("Link", back_populates="offers")