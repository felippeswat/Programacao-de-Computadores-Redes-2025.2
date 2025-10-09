from re import X
import sys
from tkinter import Y

print('Digite um numero positivo com 4 algarismos para realizar a soma dos seus algarismos')

Numero      =int(input('Digite o numero inteiro com 4 algarismos'))

if not (Numero >0) and (Numero < 10000):
    sys.exit('Valor do numero inválido!')

w           = Numero % 10
numero      = Numero // 10
x           = numero % 10
numero      = numero // 10
y           = numero % 10
z           = numero // 10

print(f'W {w}, X {x}, Y {y}, Z {z}')

resultado       = w + x + y + z

print(f'O resultado da soma dos algarios de {Numero} é: {resultado}')