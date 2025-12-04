lstValores = list()

for i in range(1, 21):

    x = 1

    for j in range(1, i +1):

        x *= j

    lstValores.append([i, x])


arqSaida = open('fatoriais2a.txt', 'a')

for lista in lstValores:

    arqSaida.write(f'{lista[0]} ; {lista[1]}\n')


arqSaida.close