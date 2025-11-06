

num = int(input('digite um numero'))

if (- 1 + (1 + 8 * num) ** 0.5) % 2 == 0:

    posicao     =   (- 1 + (1 + 8 * num) ** 0.5) / 2

    print(f'{num} é triangular e sua posição é {posicao}')

else:
    print(f'{num} não é trinagular!')
