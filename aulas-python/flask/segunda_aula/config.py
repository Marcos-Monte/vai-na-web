from os import environ # Traz para o arquivo o acesso as variaveis de ambiente
from dotenv import load_dotenv # Traz a função para carregar as variaveis de ambiente nesse arquivo

load_dotenv() # Carrega as variaveis de ambiente do arquivo .env

print("URI do banco:", environ.get('URL_DATABASE_DEV'))

class Config:
    SQLALCHEMY_DATABASE_URI = environ.get('URL_DATABASE_DEV')
    SQLALCHEMY_TRACK_MODIFICATIONS = False