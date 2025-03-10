''' TUPLAS:

- Depois de criadas, não podem ser alteradas
- São imutáveis
- São ordenadas
- Valores acessados por índices
- Podem conter qualquer tipo de dado
- Ocupa menos espaço na memória
    - Em comparação com as listas que precisam de mais espaço
- São mais rápidas
- São mais seguras
- São usadas para dados que não podem ser alterados
- Utilizar quando:
    - Precisar proteger os dados
    - Acessar os dados mais rapidamente
'''
# Se assemelha ao 'const' do JavaScript
# Se tem parênteses é uma tupla
# Não precisa ser do mesmo tipo (heterogênea)
minha_tupla = (
    'josefina',
    '123.123.456-78',
    'Rua das Flores, 123',
)

print(minha_tupla)
print('*'*100)

print(minha_tupla.index('123.123.456-78'))
print(minha_tupla.count('Rua das Flores, 123'))
print(len(minha_tupla))
print('*'*100)

print('Intervalos de Impressão: ')

# Valor inicial 'sempre' será o indice
# Segundo valor tem duas opções
# - Se o primeiro valor for vazio = Quantidade de elementos
# - Se o primeiro valor for preenchido = Intervalo de elementos

# Intervalos entre o começo e mostra a quantidade de 2 elementos
print(minha_tupla[:2])

# Intervalos entre o segundo elemento e o final
print(minha_tupla[1:])


# Empacotamento Implicito
numeros = 1, 2, 3, 4, 5
print(type(numeros))