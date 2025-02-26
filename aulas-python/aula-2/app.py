# Depois que uma variavel é atribuída com uma String, ela não pode mais ser alterada, sem ser destruída.
# Para alterar alguma coisa, fazemos uma 'cópia' e alterar o valor mostrado ou que será armazenado em outro lugar
verdade = 'Python é incrível'
print(verdade)
# lower, retorna uma cópia da string em letras minusculas
print(verdade.lower())
# upper , retorna uma cópia da string em letras maiusculas
print(verdade.upper())
# capitalize, retorna uma cópia da string em com apenas o primeiro caractere de cada palavra em maiúsculo
print(verdade.capitalize())
# replace, modifica um valor por outro
print(verdade.replace('Python', 'JavaScript'))
# split, separa uma lista baseado no 'caractere' indicado
print(verdade.split(' '))

