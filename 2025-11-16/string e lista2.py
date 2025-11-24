pares = []

for vez in range(3):
    menor   =   int(input('Digite o menor número: '))
    maior   =   int(input('Digite o maior número: '))

    pares.append((menor, maior))
    print('Guardei!', (menor, maior))


print(f'\n todos os pares {pares}')