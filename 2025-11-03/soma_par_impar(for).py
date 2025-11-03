
# Inicialização das variáveis.
intSomaPares   = 0
intSomaImpares = 0

# Laço FOR de 1 a 100.
for intContador in range(1, 101):

# Verifica se o número é par ou ímpar e acumula a soma.
    if intContador % 2 == 0:
        intSomaPares += intContador
    else:
        intSomaImpares += intContador

# Exibição dos resultados.
print(f'Soma dos números pares....: {intSomaPares}')
print(f'Soma dos números ímpares .: {intSomaImpares}')