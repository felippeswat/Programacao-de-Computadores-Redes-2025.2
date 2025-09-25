from codecs import BufferedIncrementalDecoder
from hashlib import algorithms_guaranteed
from subprocess import BELOW_NORMAL_PRIORITY_CLASS


print('Vamos calcular a área de um trapézio! ')

Bmenor      =float(input('Informe a base menor do trapézio: '))
Bmaior      =float(input('Informe a base maior do trapézio: '))
altura      =float(input('informe a base do trapézio: '))


area        =(( Bmaior + Bmenor ) * altura) / 2

#print(f'A área do trapezio é: {area:.4}')
#print(f'A área do trapezio é: {area:.3}')
#print(f'A área do trapezio é: {area:.2}')
print(f'A área do trapezio é: {area}')
