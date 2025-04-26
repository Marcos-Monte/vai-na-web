from src.model import db # Traz a instancia SQLAlchemy para este arquivo
from sqlalchemy.schema import Column # Traz recurso que transforma atributos em colunas
from sqlalchemy.types import String, DECIMAL, Integer # Traz o recurso que identifica os tipos de dados para as colunas

# Ess classe é uma abstração de todos os colaboradores
class Colaborador(db.Model): # db.Model -> Mapear e criar a tabela  
    __tablename__ = 'tb_colaborador' # Cria a tabela com o nome tb_colaborador
    
    # Atributos da classe
    # id INT AUTO_INCREMENT PRIMARY KEY
    id = Column(Integer, primary_key= True, autoincrement=True) # Coluna id, tipo inteiro, chave primaria com autoincremento
    
    nome = Column(String(255))
    email = Column(String(155))
    senha = Column(String(50))
    cargo = Column(String(50))
    salario = Column(DECIMAL(2))
    
    # Método __init__ é um método construtor
    def __init__ (self, nome, email, senha, cargo, salario):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.salario = salario
        
# -------------------------------------------------------------------------------------------------
    # Formata o tipo de dados que serão enviados ao FrontEnd
    def to_dict(self) -> dict:
        return {
            'email': self.email,
            'senha': self.senha,
            'salario': self.salario,
            'cargo': self.cargo,
        }
        
#-------------------------------------------------------------------------------------------------
    # Pega um Objeto e transforma em um Dicionário
    def all_data(self) -> dict:
        return {
            'id': self.id,
            'nome': self.nome,
            'cargo': self.cargo,
            'salario': self.salario,
            'email': self.email,
            'senha': self.senha,
        }