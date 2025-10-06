import sys

try:
   intDividendo = int(input('Informe o Dividendo: '))
   intDivisor = int(input('Informe o Divisor..: '))
   quociente = intDividendo / intDivisor

except ZeroDivisionError:
   sys.exit('ERRO: Divisão por Zero não é permitida...')

except ValueError:
  sys.exit('ERRO: Informe apenas números inteiros...')

except Exception as strErro:
   sys.exit(f'EXCEÇÃO: {sys.exc_info()[0]} -> {strErro}')

else:
   print(f'{intDividendo} / {intDivisor} = {quociente:.2f}')

