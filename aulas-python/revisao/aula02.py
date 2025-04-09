# Dicionários

banco_de_dados = [
    {'id': 1, 'nome': 'Xaropinho', 'cargo': 'Gerente de vendas'},
    {'id': 2, 'nome': 'Naruto Uzumaki', 'cargo': 'Especialista em IA'},
    {'id': 3, 'nome': 'Caroline Mota', 'cargo': 'CTO'},
    {'id': 4, 'nome': 'Alessandra Cotta', 'cargo': 'CEO'}
]

# print(banco_de_dados[0])
# print(banco_de_dados[1])
# print(banco_de_dados[2])
# print(banco_de_dados[3])

for colaborador in banco_de_dados:
    print(f'Colaborador(a): {colaborador['nome']}')

print('*'*30)

i = 0
while i < len(banco_de_dados):
    nome = banco_de_dados[i]['nome']
    print(f'Colaborador(a): {nome}')
    i = i + 1