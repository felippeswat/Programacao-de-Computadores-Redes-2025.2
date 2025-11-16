import sys

strTexto   =   input('Digite uma palavra: ')

if ' ' in strTexto:
    sys.exit('Você digitou mais de uma palavra!')

strTextoinvert   =   strTexto[::-1]

print(strTexto)
print(strTextoinvert)

if strTexto.lower == strTextoinvert.lower:
    
    print('São palindromos')

else:
    print('Não são Palindromos')