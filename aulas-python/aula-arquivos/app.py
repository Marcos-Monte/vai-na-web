'''Sistema de Cadastro de Arquivo'''

import csv # manipulação de arquivos CSV
import time # Timer 
import os # manipulação do sistema operacional

print('-'*100)
nome_completo = input('Digite o nome completo: ')
print('-'*100)
data_nascimento = input('Digite a data de nascimento: (DD/MM/AAAA) ')
print('-'*100)
cpf = input('Digite o CPF: (exemplo: ###.###.###-##) ')


# Verificando se o arquivo já existe
with open('ficha_cadastro.csv', mode='a', newline='') as arquivo: # 'a' para append, 'w' para write, 'r' para read
    # Objeto para escrita no arquivo
    escritor = csv.writer(arquivo)
    # Escrevendo no arquivo
    escritor.writerow([nome_completo, data_nascimento, cpf])

print('-'*100)
print('* Cadastro realizado com sucesso! *')
print('-'*100)
# Timer para limpar a tela
os.system('cls')

#  Timer para limpar a tela
for i in range(3):
    print(f'Gerando o arquivo em {i+1} segundos')
    # Time
    time.sleep(1)
    # Limpar a tela
    os.system('cls')


with open('ficha_cadastro.csv', mode='r') as arquivo:
    dados = csv.reader(arquivo)
    for linha in dados:
        print(linha)