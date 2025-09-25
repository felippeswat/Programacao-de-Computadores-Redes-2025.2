from cgi import print_arguments
from re import M
from statistics import median


print('Vamos calcular a média entre dois números: ')

N       =float(input('Informe o primeiro número: '))
M       =float(input('Informe o segundo número '))

media   =(N + M)/2

print(f'A média entre {N} e {M} é: {media}')