'''
   Programa que solicita um número inteiro ao usuário e exiba os n
   primeiros elementos da Série de Fibonacci (usando WHILE).

   Exemplo: n = 10

   Saída: 
      1, 1, 2, 3, 5, 8, 13, 21, 34, 55
'''

# Importando a biblioteca sys.
from pickletools import ArgumentDescriptor
import sys

# Entrada de dados do usuário com tratamento de erro.
try:

    intNumero = int(input('Informe um valor inteiro maior que 1: '))

# Tratamento de erro pra valores não numéricos.
except ValueError:
    sys.exit('ERRO: O valor informado deve ser inteiro...')

# Tratamento para outros tipos de erro.
except:
    sys.exit(f'ERRO: {sys.exc_info()}')

# Verificando se o valor da entrada é possitivo.
else:
    if intNumero < 1:
        sys.exit('ERRO: digite um numero maior que 1')

# Verificando se o valor da entrada é zero ou um.
    if intNumero == 1 or intNumero == 2:
        sys.exit(f' o elemento numero {intNumero} da sequencia fibonacci é = 1')

    auxiliar  = 0
    atual     = 1
    anterior  = 0
    proximo   = 0
    
while auxiliar < intNumero:
    print(f'{sequencia}')
    
    atual = sequencia + anterior
    anterior  = sequencia

    auxiliar += 1