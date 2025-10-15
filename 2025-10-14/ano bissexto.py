'''
   Escreva um programa que pede ao usuário para inserir um ano e 
   determina se ele é bissexto ou não. 
   
   Um ano é bissexto se atender a uma das seguintes regras:

      - É divisível por 4, mas não é divisível por 100.

      - É divisível por 400.

      (Por exemplo, 2000 e 2400 são bissextos; 1800, 1900 e 2100 não são). 
      
   O programa deve exibir "O ano [ano] é bissexto." ou 
   "O ano [ano] não é bissexto.". 
   
   Use try...except para validar a entrada.
'''
import sys

# Entrada de dados com tratamento de erro
try:
   
   ano     =   int(input('Informe o ano com 4 digitos: '))

# Tratamento de erro para valores não numéricos
except ValueError:
   
   sys.exit('ERRO: Você deve digitar um valor numérico.')

# Tratamento de erro para outros tipos de erro
except Exception as strErro:
   sys.exit(f'ERRO: {strErro}')
 
else:

# Verifica se o ano e um valor negativo 
   if ano < 0:
      sys.exit('ERRO: O ano deve ser um valor numerico, inteiro e positivo.')

#Verificando se o ano é bissexto
if ano % 100 == 0:

    print(f'o ano de {ano} é bissexto!')

else:

    print(f'o ano de {ano} não é bissexto!')