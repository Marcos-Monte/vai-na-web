#  Da bilbioteca flask me traga a classe Flask()
from flask import Flask

# App = carregar todos os recursos NESTE ARQUIVO
# Dunder names, métodos especiais para o python -> __exemplo__
app = Flask(__name__) #  __name__ -> (Identifica o Arquivo)

# Criar uma rota
@app.route('/') 
# Associar a rota a uma função (apenas colocando as duas juntas)
def hello():
    # Toda rota criada precisa ter uma função com um retorno
    return '<h1>Hello, World! Marcos</h1>'

# Criar uma rota
@app.route('/dados')
# Associar a rota a uma função (apenas colocando as duas juntas)
def mostrar_dados():
    # Criando um dicionario que será retornado
    dados = {'nome': 'Marcos Monte', 'cpf': '123.456.789-10', 'cargo': 'Desenvolvedor Web'}
    return dados

# Se identificar o __arquivo__ como '__principal__', você executa
if __name__ == '__main__':
    app.run(debug=True) # Debug=True, indica que tudo o que for atualizado aqui no Servidor, será atualizado no Navegador

