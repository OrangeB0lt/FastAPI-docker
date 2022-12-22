from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from os import environ


p_user = environ.get('POSTGRES_USER')
p_password = environ.get('POSTGRES_PASSWORD')
p_host = environ.get('POSTGRES_HOST')
p_port = environ.get('POSTGRES_PORT')
p_db = environ.get('POSTGRES_DB')

DATABASE_URL = f"postgresql+psycopg2://{p_user}:{p_password}@{p_host}:{p_port}/{p_db}"

engine = create_engine(URL(**DATABASE_URL))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(Integer, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    