from cmath import pi


print('Vamos calcular a área de um círculo!')

raio        =float(input('Informe o raio do círculo a ser calculado: '))
pi          =3.1416
area        =pi * (raio ** 2)

print (f'A área do circulo de ráio {raio} é: {area}')
#print (f'A área do circulo de ráio {raio} é: {area:.3f}')
print (f'A área do circulo de ráio {raio} é: {area:.2f}') #para limitar as casas decimais utilizamos (:.2f) após a variável a ser exibida, neste caso limitamos em duas casas decimais.
#print (f'A área do circulo de ráio {raio} é: {area:.1f}')   