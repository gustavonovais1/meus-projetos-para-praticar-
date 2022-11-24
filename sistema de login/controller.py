from fastapi import FastAPI
from model import CONN, Usuarios
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

def retornaSession():
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

@app.post('/cadastar')
def cadastar(nome: str, user: str, senha: str):
    session = retornaSession()
    usuario = session.query(Usuarios).filter_by(usuario=user).all()
    if len(usuario) == 0:
        x = Usuarios(nome=nome, usuario=user, senha=senha)
        session.add(x)
        session.commit()
        
        return 1
    elif len(usuario) > 0:
        return 2

@app.post('/logar')
def logar(user, senha):
    session = retornaSession()
    usuario = session.query(Usuarios).filter_by(usuario=user, senha=senha).all()
    if len(usuario) > 0:
        return 3 
    elif len(usuario) == 0:
        return 4 

@app.post('/listar')
def listar():
    session = retornaSession()
    x = session.query(Usuarios).all()
    for i in x:
        print(i.usuario)

