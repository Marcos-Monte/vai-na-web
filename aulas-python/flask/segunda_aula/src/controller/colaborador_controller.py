# Recebe as Requisições e Devolvemos as Respostas da Entidade 'Colaborador'
from flask import Blueprint, request, jsonify
# Request -> Recurso do flask que facilita a captura dos dados na requisição. Toda Req tem o JSON, através do 'request' pegamos e armazenamos em uma variavel
    # Trabalhar com as requisições
# Jsonify -> Recurso do flask que envia os dados no formato Json
    # Oposto do Request, trabalha com a Resposta -> Envio dos Dados no Formato JSON, Envio dos Status (200, 404, 500...)

from src.model.colaborador_model import Colaborador # Importa a classe molde de Colaborador
from src.model import db # Importa a instância do banco de dados

dados = [
    {'id': 1, 'nome': 'Karynne Moreira', 'cargo': 'CEO', 'cracha': '010101'},
    {'id': 2, 'nome': 'Samuel Silverio', 'cargo': 'CTO', 'cracha': '215487'},
    {'id': 3, 'nome': 'Wisney Oliveira', 'cargo': 'Desenvolvedor Back-end', 'cracha': '147852'},
    {'id': 4, 'nome': 'Romulo Rosa', 'cargo': 'DEVOPS', 'cracha': '171171'},
    {'id': 5, 'nome': 'Marcos Monte', 'cargo': 'QA', 'cracha': '000000'},
]

# Blueprint -> Conceito de dividir as rotas 
# Usar o nome do arquivo, recebe a Classe 'Blueprint'
bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador') # https://localhost:8000/colaborador

@bp_colaborador.route('/pegar-dados')
def pegar_dados():
    # Criando uma lista de objetos de Colaboradores
    return dados # Uma rota sempre retorna algo

# Rota cadastrar só vai receber requisições com o método POST
@bp_colaborador.route('/cadastrar', methods=['POST']) # Colchetes indica que o retorno pode ser uma lista
def cadastrar_novo_coladorador():
    
    dados_requisicao = request.get_json()
    
    # if not dados_requisicao:
    #     return jsonify({'error': 'Necessário enviar dados!'}), 400
    
    # novo_colaborador = {
    #     'id': len(dados) + 1,
    #     'nome'.lower(): dados_requisicao['nome'],
    #     'cargo': dados_requisicao['cargo'],
    #     'cracha': dados_requisicao['cracha'],
    # }
    
    # dados.append(novo_colaborador)
    
    novo_colaborador = Colaborador(
        nome=dados_requisicao['nome'],
        email=dados_requisicao['email'],
        senha=dados_requisicao['senha'],
        cargo=dados_requisicao['cargo'],
        salario=dados_requisicao['salario']
    )
    
    # INSERT INTO tb_colaborador (nome, email, senha cargo, salario) 
    # VALUES (
        # dados_requisicao['nome'], dados_requisicao['email'], dados_requisicao['senha'], dados_requisicao['cargo'], dados_requisicao['salario']
    #)
    db.session.add(novo_colaborador)
    db.session.commit() # Faz o commit no banco de dados, persistindo os dados
    
    return jsonify({'response': 'Colaborador cadastrado com sucesso'}), 201 # Retorna mensagem de sucesso e o Status Code de 'created'

# SInaliza que os dados enviados após o 'atualizar', serão dinamicos e enviados pela URL
# https://localhost:8000/colaborador/atualizar/500 --> O ID deve estar passando assim
@bp_colaborador.route('/atualizar/<int:id_colaborador>', methods=['PUT'])
def atualizar_dados_colaborador(id_colaborador):

    dados_requisicao = request.get_json()
    
    for colaborador in dados:
        if colaborador['id'] == id_colaborador:
            colaborador_encontrado = colaborador
            break
        else:
            return jsonify({'response': 'Id de usuário não identificado'}), 404
        
    if 'nome' in dados_requisicao:
        colaborador_encontrado['nome'] = dados_requisicao['nome']
        
    if 'cargo' in dados_requisicao:
        colaborador_encontrado['cargo'] = dados_requisicao['cargo']
    
    return jsonify({'response': 'Dados do colaborador atualizado com sucesso'}), 200