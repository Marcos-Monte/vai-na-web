# Listas

# Agrupam muitos valores juntos ; Permitem duplicatas ; Podem ser de tipos diferentes ; São mutáveis
lista_alunos = ['Amanda Costa', 'Felipe Preira', 'Caroline Caetano', 'Eduardo Gomes', 'Romulo Rosa', 8, 'Amanda Costa',]
print(lista_alunos)

# Adiciona um elemento no final da lista
lista_alunos.append('Suelen Braga')
lista_alunos.append('Suelen Braga')
print(lista_alunos)

# Mostra o tamanho da lista
print(f'Tamanho da Lista: {len(lista_alunos)}')

# Remove o primeiro elemento que corresponde ao valor especificado
lista_alunos.remove('Amanda Costa')
print(lista_alunos)

# Remove o elemento com o indice indicado
lista_alunos.pop(lista_alunos.index('Suelen Braga'))
print(lista_alunos)

print(f'O elemento aparece {lista_alunos.count('Suelen Braga')} vezes')


# Tupla
# Existem apenas o 'count' e o 'index' como métodos
minha_tupla = ('Samuel', 19, 1.87)

print(type(minha_tupla))

# Dicionários

meu_dicionario = {'nome': 'Marcos', 'idade': 36}
print(meu_dicionario)
