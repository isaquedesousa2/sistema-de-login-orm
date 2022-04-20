from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Pessoa
import hashlib

def retorna_session():
    CONNECTION=f'sqlite:///base.db'
    engine = create_engine(CONNECTION, echo=False)
    Session = sessionmaker(bind=engine)
    return Session()


class Controller_Cadastro:
    
    @classmethod
    def verfica_dados(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 3:
            return 2
        if len(email) > 100:
            return 3
        if len(senha) > 128 or len(senha) < 8:
            return 4

        return 1

    @classmethod
    def cadastrarUsuario(cls, nome, email, senha):
        session = retorna_session()
        usuario = session.query(Pessoa).filter(Pessoa.email==email).all()

        if usuario:
            return 5
        
        dados_verificados = cls.verfica_dados(nome, email, senha)

        if dados_verificados != 1:
            return dados_verificados
        
        try:
            senha = hashlib.sha512(senha.encode()).hexdigest()
            x = Pessoa(nome=nome, email=email, senha=senha)
            session.add(x)
            session.commit()
            return 1
        except:
            return 3


class Controller_Login:
    
    @classmethod
    def login(cls, email, senha):
        session = retorna_session()
        senha = hashlib.sha512(senha.encode()).hexdigest()
        usuario = session.query(Pessoa).filter(Pessoa.email == email).filter(Pessoa.senha == senha).one()
        if usuario:
            return {'logado': True, 'id': usuario.id}
        else:
            return False
