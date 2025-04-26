# Recebe as Requisições e Devolvemos as Respostas da Entidade 'Colaborador'
from flask import Blueprint, request, jsonify
# Request -> Recurso do flask que facilita a captura dos dados na requisição. Toda Req tem o JSON, através do 'request' pegamos e armazenamos em uma variavel
    # Trabalhar com as requisições
# Jsonify -> Recurso do flask que envia os dados no formato Json
    # Oposto do Request, trabalha com a Resposta -> Envio dos Dados no Formato JSON, Envio dos Status (200, 404, 500...)

from src.model.colaborador_model import Colaborador # Importa a classe molde de Colaborador
from src.model import db # Importa a instância do banco de dados

from src.security.security import checar_senha, hash_senha

# Anteriormente usava se uma lista de dicionario com dados como banco de dados Mockado

# Blueprint -> Conceito de dividir as rotas 
# Usar o nome do arquivo, recebe a Classe 'Blueprint'
bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador') # https://localhost:8000/colaborador

@bp_colaborador.route('/todos-colaboradores')
def pegar_dados_todos_colaboradores():
    # Criando uma lista de objetos de Colaboradores
    # return dados # Uma rota sempre retorna algo
    # Instancia do Banco de Dados = db
    colaboradores = db.session.execute(
        db.select(Colaborador) # Classe Colaborador é o molde para criar a tabela
    ).scalars().all() # AO inves de trazer 1 dado trás todos 
    
    colaboradores = [ colaborador.all_data() for colaborador in colaboradores ]  # Está adicionando cada colaborador dentro do Dicionário Colaboradores
    # Execute essa expressão, para cada          item do         iteravel
    return jsonify(colaboradores), 200

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
        senha=hash_senha(dados_requisicao['senha']),
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
    
    colaborador = db.session.get(Colaborador, id_colaborador)

    if not colaborador:
        return jsonify({'response': 'Id de usuário não identificado'}), 404

    if 'nome' in dados_requisicao:
        colaborador.nome = dados_requisicao['nome']
    if 'cargo' in dados_requisicao:
        colaborador.cargo = dados_requisicao['cargo']
    if 'salario' in dados_requisicao:
        colaborador.salario = dados_requisicao['salario']

    db.session.commit()

    return jsonify({'response': 'Dados do colaborador atualizados com sucesso'}), 200

@bp_colaborador.route('login', methods=['POST'])
def login():
    
    dados_requisicao = request.get_json()
    email = dados_requisicao['email']
    senha = dados_requisicao['senha']
    
    if not email or not senha:
        return jsonify({'mensagem': 'Todos os campos devem ser preenchidos'}), 400
    
    colaborador = db.session.execute(
        # Query fica dentro dos parametros do 'execute'
            # (Classe Colaborador está dentro de 'model')
        db.select(Colaborador).where(Colaborador.email == email) # Select * from colaborador Where email == 'algum_email
        
    ).scalar() # Traz um registro ou Atribui 'none' na variável
    
    if not colaborador:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 236
    
    colaborador = colaborador.to_dict()
    
    if email == colaborador.get('email') and checar_senha(senha, colaborador.get('senha')):
        return jsonify({'mensagem': 'Login realizado com sucesso'}), 200