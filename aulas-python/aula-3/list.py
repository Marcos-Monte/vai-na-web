''' LISTAS:

- Estrututa de dadoss mutáveis
- Ordenadas
- Valores acessados por índices
- Podem conter qualquer tipo de dado
'''
# Se tem colchetes é uma lista
# Não precisa ser do mesmo tipo (heterogênea)
minha_lista = ['A procura da Felicaide', 'Escritores da Liberdade', 'Jogo da Imitação', 'Matrix', 'Sherek', 'Pequena Sereia', 'Estrelas além do Espaço', 'O menino do pijama listrado']

# Lista Iniical
print(minha_lista)

print('*'*100)

# Método de adição de elementos, normalmente no final da lista
minha_lista.append('O rapto do menino dourado')

# Lista Atualizadas
print(minha_lista)
print('*'*100)

# Método de Ordenação de Listas, não pode ter tipos diferentes. Exemplo: int e str
# Apenas se converter todos os elementos para str
minha_lista.sort()

# Lista Reordenada
print(minha_lista)
print('*'*100)

# Método de Remoção de Elementos, se errar o nome do elemento, dará erro
# Se tiver mais de um elemento com o mesmo nome, removerá o primeiro
# Ao encontrar o elemento, ele remove e para de procurar
minha_lista.remove('Pequena Sereia')

# Lista Atualizadas
print(minha_lista)
print('*'*100)

# Método que indica quantas vezes um elemento aparece na lista
print('Qtde de vezes que o filme Matrix, aparece na lista: ', minha_lista.count('Matrix'))
print('*'*100)

# Método de Inserção de Elementos, adiciona um elemento em uma posição específica
# O primeiro parâmetro é a posição e o segundo é o elemento
minha_lista.insert(0, 'Um sonho de liberdade')

# Lista Atualizadas
print(minha_lista)
print('*'*100)

# Método de Remoção de Elementos, remove o último elemento da lista
minha_lista.pop(0)
# Se informar o índice, ele remove o elemento da posição informada
minha_lista.pop()

# Printar o indice de um elemento da lista
print('Indice do Elemento: ', minha_lista.index('O rapto do menino dourado'))
print('*'*100)

# Lista Atualizadas
print(minha_lista)
print('*'*100)

# Printar o tamanho da lista
print('Tamanho da Lista: ', len(minha_lista))
print('*'*100)

for filme in minha_lista:
    print(filme)
