import os

lstValores = list()

for i in range(1, 21):

    x = 1

    for j in range(1, i +1):

        x *= j

    lstValores.append([i, x])

strNomeDir = os.path.dirname(__file__)

strNomeArqivo = f'{strNomeDir}\\fatoriais3.txt'
arqSaida = open(strNomeArqivo, 'w')

for lista in lstValores:

    arqSaida.write(f'{lista[0]} ; {lista[1]}\n')


arqSaida.close