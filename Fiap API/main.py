import time
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Facility, Address, Gateway, Tracker, Location, CONN
from datetime import datetime


app = FastAPI()


def conectaBanco():
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

@app.post('/facility')
def facility(nome: str):
    try:
        print('ok')
        session = conectaBanco()
        faci = session.query(Facility).filter_by(nome=nome).all()
        print(faci)
        if len(faci) == 0:
            create_time = datetime.fromtimestamp(time.time())
            update_time = datetime.fromtimestamp(time.time())
            x = Facility(nome=nome, created_at=create_time, update_at=update_time)
            session.add(x)
            session.commit()
            return {'status': 'SUCESSO'}
        elif len(faci) > 0:
            return {'status': 'Nome já cadastrado'}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'status': 'ERROR'}


@app.get('/facilities')
def get_facilities():
    try:
        session = conectaBanco()
        facilities = session.query(Facility).all()
        return {'facilities': [f.nome for f in facilities]}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'status': 'ERROR'}


@app.get('/facility/{id}')
def get_facility(id: int):
    try:
        session = conectaBanco()
        facility = session.query(Facility).get(id)
        if facility is None:
            return {'status': 'Facility not found'}
        else:
            return {'facility': facility.nome}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'status': 'ERROR'}
