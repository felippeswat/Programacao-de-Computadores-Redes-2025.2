from io import RawIOBase
import sys

Dividendo        =int(input('Informe o Dividendo: '))
Divisor          =int(input('Informe o divisor: '))

try:
    resultado       = Dividendo/Divisor

except Exception as e:
    print(f'Erro: {e}')
else:
    print(f'resultado: {resultado}')
