# Para que a biblioteca encontre o arquivo de test ele tem que encontrar com 'test'

##### Para Rodar devemos usar no terminal --> pytest src/tests/test_app.py

# pip install pytest-flask -> iNSTALANDO O PYTEST
import pytest # Traz a biblioteca de testes
import time # Manipular o tempo
from src.model.colaborador_model import Colaborador
from src.app import create_app

# ------------------------------------
# Configurações para Testes


# Yield será o primeiro a ser destruído para liberar espaço de memotira
@pytest.fixture # Identifica funções de configurações para o teste
def app():
    app = create_app() # Instancia do Flask
    yield app # YIELD vai guardar os valores em memoria (para usar em outros lugares)
    
    
@pytest.fixture
def client(app): # Simula o Usuário
    return app.test_client()
    
# --------------------------------------

# Arquivos e Funções precisam começar com a palavra test
def test_desempenho_requisicao_get(client):
    
    comeco = time.time() # Pega a hora atual e transforma em segundos
    
    for _ in range(1900): # fazer 100 requisições em 1 segundo (_ fala que a variavel auxiliar não serve para nada)
        resposta = client.get('/colaborador/todos-colaboradores') # Usuario vai fazer um get no servidor e armazenar em 'resposta'
        
    fim = time.time() - comeco # A hora que acabar menos a hora que começou (dando o o tempo que levou para fazer a requisição)
    assert  fim < 1.0 # Assert -> Palavra reservada Verifica condições (Verifica se elas são iguais)
    