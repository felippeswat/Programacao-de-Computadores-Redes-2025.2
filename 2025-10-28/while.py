


numero  =   1
par     =   0
impar   =   0

while numero <= 100:
    if numero % 2 == 0:
        par += numero

    else:
        impar += numero

    numero += 1

print(f'A soma dos pares é: {par}')
print(f'A soma dos impares é: {impar}')