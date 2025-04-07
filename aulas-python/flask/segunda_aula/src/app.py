# Responsavel pela criação da aplicação
# Create_app() -> Vai configurar a instancia do Flask
from flask import Flask
from src.controller.colaborador_controller import bp_colaborador
from src.model import db # Importa a instância do banco de dados
from config import Config # Importa a classe de configuração

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_colaborador) # Registra o blueprint
    
    app.config.from_object(Config) # Traz a configuração do ambiente de desenvolvimento
    db.init_app(app) # Inicia a conexão com o Banco de Dados
    
    with app.app_context():
        db.create_all() # Cria as tabelas caso elas não existam
    
    return app

