from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

BANCO = 'TesteAPI1.db'


CONN = f"sqlite:///{BANCO}"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Facility(Base):
    __tablename__ = 'Facility'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    nome = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow())
    update_at = Column(DateTime, default=datetime.utcnow())


class Address(Base):
    __tablename__ = 'Address'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    facility_id = Column(Integer, ForeignKey('Facility.id'), nullable=False)
    street = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    zipcode = Column(String(50), nullable=False)

class Gateway(Base):
    __tablename__ = 'Gateway'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = nome = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    update_at = Column(DateTime, default=datetime.utcnow())
    last_connection = Column(DateTime, default=datetime.utcnow())
    facility = Column(Integer, ForeignKey('Facility.id'), nullable=False)


class Tracker(Base):
    __tablename__ = 'Tracker'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    update_at = Column(DateTime, default=datetime.utcnow())
    last_connection = Column(DateTime, default=datetime.utcnow())
    facility = Column(Integer, ForeignKey('Facility.id'), nullable=False)


class Location(Base):
    __tablename__ = 'Location'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    tracker_id = Column(Integer, ForeignKey('Tracker.id'), nullable=False)
    longitude = Column(Float)
    latitude = Column(Float)
    update_at = Column(DateTime, default=datetime.utcnow())


Base.metadata.create_all(engine)
