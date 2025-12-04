lstValores = list()

for i in range(1, 21):

    x = 1

    for j in range(1, i +1):

        x *= j

    lstValores.append([i, x])


arqSaida = open('fatoriais.txt', 'w')

arqSaida.write(str(lstValores))


arqSaida.close