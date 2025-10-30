'''
   Fazer um programa que solicite um número inteiro (n) e exiba os 
   n primeiros elementos da sequência de Fibonacci.

   Exemplo: n = 10

   Saída: 
      1, 1, 2, 3, 5, 8, 13, 21, 34, 55
'''

import sys

try:

    numero  =   int(input('Digite um numero para somar os primeiros elementos da sequência Fibonacci'))

except ValueError:
    sys.exit('Erro, o valor perecisa ser positivo')
