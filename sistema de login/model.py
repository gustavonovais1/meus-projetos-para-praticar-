from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = 'root'
SENHA = '222545'
HOST = 'localhost'
BANCO = 'projeto-login'
PORT = '3306'

CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'

engine = create_engine(CONN, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'Usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(30))
    usuario = Column(String(50))
    senha = Column(String(15))

Base.metadata.create_all(engine)