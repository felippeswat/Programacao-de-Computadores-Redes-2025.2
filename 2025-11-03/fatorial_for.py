'''vamos desenvolver um código para calcular o faturial de um numero fornecido pelo usuário'''

# Importando a biblioteca sys.
import sys

# Entrada de dados do usuário com tratamento de erro.
try:

    intNumero = int(input('Informe um valor inteiro: '))

# Tratamento de erro pra valores não numéricos.
except ValueError:
    sys.exit('ERRO: O valor informado deve ser inteiro...')

# Tratamento para outros tipos de erro.
except:
    sys.exit(f'ERRO: {sys.exc_info()}')

# Verificando se o valor da entrada é possitivo.
else:
    if intNumero < 0:
        sys.exit('ERRO: Não existe fatorial de número negativo...')

# Verificando se o valor da entrada é zero ou um.
    if intNumero == 0 or intNumero == 1:
        sys.exit(f'{intNumero}! = 1')

    intFatorial = 1

# Usando for com range(intNumero, 1, -1).
    for intauxiliar in range(intNumero, 1, -1):
        intFatorial *= intauxiliar

    print(f'{intNumero}! = {intFatorial}')