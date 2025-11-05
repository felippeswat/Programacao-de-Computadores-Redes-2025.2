'''Vamos desenvolver um código para testar se um numero é primo ou não!'''

# Importando a biblioteca sys.
import sys

# Entrada de dados do usuário com tratamento de erro.
try:

    numero = int(input('Informe um valor inteiro maior que zero: '))

# Tratamento de erro pra valores não numéricos.
except ValueError:
    sys.exit('ERRO: O valor informado deve ser inteiro e maior que zero!...')

# Tratamento para outros tipos de erro.
except:
    sys.exit(f'ERRO: {sys.exc_info()}')

# Verificando se o valor da entrada é possitivo.
else:

    if numero < 2:
        print(f'O númeor {numero} não é primo pois é menor que 2!')

    elif numero == 2:
        print(f'{numero} é Primo')

    elif numero % 2 == 0:
        print(f'{numero} não é primo, pois é par e maior que 2!')
        