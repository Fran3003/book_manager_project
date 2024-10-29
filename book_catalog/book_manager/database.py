from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

def get_engine(db_url='sqlite:///:memory:'):
    return create_engine(db_url)

def get_session(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()