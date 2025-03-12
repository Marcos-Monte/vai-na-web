'''Dicionarios -> Correspondente ao Objeto em JS'''
# { Chave: Valor, Chave: Valor }
#  - Chave é única e imutável, normalmente será encontrada como uma string.

dados_pessoais = {
    'nome_completo': 'Kleber Matos',
    'cpf': '123.456.789-00',
    'email': 'klebimprefeito@gmail.com',
}
print('*'*100)
# Percorrendo o dicionário e executando ações para cada item dentro do dicionario/objeto
for chave in dados_pessoais:
    print(f'{chave}: {dados_pessoais[chave]}')

# Imprime apenas 
dados_pessoais['nome_completo'] = 'Joni Tchanga'

print('*'*100)
print(f'O nome passou a ser {dados_pessoais['nome_completo']}')

print('*'*100)
# Percorrendo o dicionário e executando ações para cada item dentro do dicionario/objeto
for chave in dados_pessoais:
    print(f'{chave}: {dados_pessoais[chave]}')
    
print('*'*100)

# get() -> Procura a chave e retorna uma mensagem padrã caso a mesma não tenha sido encontrada
print(dados_pessoais.get('Nome_completo', 'Essa chave não existe no dicionario'))

# Retorna as chaves presentes
print(f'As chaves do dicionario são: {dados_pessoais.keys()}')

# Retorna os valores presentes
print(f'Os valores do dicionario são: {dados_pessoais.values()}')

# Valores podem ser estruturas, criamos um dicionário onde o valor da chave 'profissao' é uma lista de profissões
atualizacao = {'profissao': ['Empresario', 'Desenvolvedor', 'Instrutor', 'Prefeito', 'Designer'], 'nome_completo': 'Elvis de Bezerra Nunes'}

# Atualizando com o update com os valores do Disc 'atualizacao'. 
# - Se já existir uma chave, o valor da chave atualizado pelo novo
dados_pessoais.update(atualizacao)

print('*'*100)
for chave in dados_pessoais:
    print(f'{chave}: {dados_pessoais[chave]}')
print('*'*100)

# Deleção da chave e do valor com o del
# del dados_pessoais['profissao']
# Deleção da chave e do valor com o pop, ainda pode ser printado para retornar o valor na tela
print(
    f'Valor excluído: {dados_pessoais.pop('cpf')}'
)

# Novo método de Iteração 
for chave, valor in dados_pessoais.items():
    # Condicional verificando se o valor é do tipo 'list'
    if isinstance(valor, list):
        # Se for Lista, imprimir o valor
        for  val in valor:
            print(f'{chave}: {val}')
    else:
        # Se não for, imprimir o valor
        print(valor)
    
print('*'*100)