
# Criando a função sem parametros e sem retorno
def somar_dois_numeros(): 
    n1 = 10
    n2 = int('10')
    print(n1 + n2)

# Criando a função com parametros e sem retorno
def somar_numeros(n1: int, n2: int):
    if (type(n1) != int) or (type(n2) != int):
        print('Tipos de dados inválidos')
    else:
        print(n1 + n2)

# Criando a função sem parametros e com retorno
def somar_retorno():
    n1 = 100
    n2 = 100
    return n1 + n2

# Criando a função sem parametros e com retorno
def dividir_dois_numeros(n1, n2):
    if n2 == 0:
        return f'Não é possível dividir por {n2}'
    else:
        return n1 / n2
# Função recebe uma 'tupla'
def somar(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

resultado = somar()

print(f'Função sem parametros e sem retorno: ') 
{somar_dois_numeros()}

print(f'Função com parametros e sem retorno:  ')
{somar_numeros(5, 10)}

print(f'Função sem parametros e com retorno:  ')
print(somar_retorno())

print(f'Função com parametros e com retorno:  ')
resultado = dividir_dois_numeros(2, 0)
print(resultado)

print(f'Função com argumentos e com retorno:  ')
numeros = (2,5,8,5,11,9,6)
resultado = somar(*numeros)
print(resultado)

