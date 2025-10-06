import sys

try:
   intValor = int(input('Informe um valor inteiro: '))
    
   # Criando a exceção 'NegativeSquareRoot' para números negativos
   if intValor < 0:
       raise Exception('NegativeSquareRoot')
   
   intRaizQuadrada = intValor ** 0.5
except ValueError:
   sys.exit('ERRO: Por favor, insira apenas números inteiros.')
except Exception as strErro:
   if str(strErro) == 'NegativeSquareRoot':
       sys.exit('ERRO: Não há Raiz Real para números negativos...')
   
   sys.exit(f'ERRO: {strErro}')
else:
   print(f'A raiz quadrada de {intValor} é {intRaizQuadrada:.2f}')