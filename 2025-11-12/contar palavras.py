'''Vamos contar quantas palavras temos em uma entrada digitada pelo usário'''

strTexto        =       input('Digitem uma frase: ')

cont            =       1

for espaco in strTexto:

    if espaco == " ":
        cont +=1

print(cont)