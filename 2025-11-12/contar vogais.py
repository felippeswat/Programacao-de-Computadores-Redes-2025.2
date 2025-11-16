'''Vamos contar quantas vogais temos em uma palavra digitada pelo usário'''

strTexto        =       input('Digitem uma palavra')

vogais      =       "aeiouàèìòùáéíóúâêîôûãõ"
cont        =       0

for palavra in strTexto.lower():
    if palavra in vogais:
        cont +=1

print(cont)