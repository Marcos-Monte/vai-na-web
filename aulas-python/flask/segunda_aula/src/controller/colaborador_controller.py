# Requisições e Respostas da Entidade 'Colaborador'
from flask import Blueprint

# Blueprint -> Conceito de dividir as rotas 
# Usar o nome do arquivo, recebe a Classe 'Blueprint'
bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador') # https://localhost:8000/colaborador

@bp_colaborador.route('/pegar-dados')
def pegar_dados():
    # Criando uma lista de objetos de Colaboradores
    dados = [
        {'nome': 'Karynne Moreira', 'cargo': 'CEO', 'cracha': '010101'},
        {'nome': 'Samuel Silverio', 'cargo': 'CTO', 'cracha': '215487'},
        {'nome': 'Wisney Oliveira', 'cargo': 'Desenvolvedor Back-end', 'cracha': '147852'},
        {'nome': 'Romulo Rosa', 'cargo': 'DEVOPS', 'cracha': '171171'},
        {'nome': 'Marcos Monte', 'cargo': 'QA', 'cracha': '000000'},
    ]
    
    return dados # Uma rota sempre retorna algo



