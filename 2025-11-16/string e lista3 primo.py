pares_primos = []

for vez in range(3):
    menor   =   int(input('Digite o menor número impar maior que 2!: '))
    maior   =   menor +2

    e_primo_menor = True

    for d in range(2, menor):
        if menor % d == 0:
            e_primo_menor = False
            break
 
    e_primo_maior = True
    for d in range(2, maior):
        if maior % d == 0:
            e_primo_maior = False
            break

    if e_primo_menor and e_primo_maior:
        pares_primos.append((menor, maior))
        print("É gêmeo! Guardei:", (menor, maior))
    else:
        print('Não são primos... Ignorados.')

print('\n' + '='*40)
print(f'\n todos os pares {pares_primos}')