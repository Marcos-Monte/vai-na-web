# Responsavel pela criação da aplicação
# Create_app() -> Vai configurar a instancia do Flask
from flask import Flask

def create_app():
    app = Flask(__name__)
    return app

