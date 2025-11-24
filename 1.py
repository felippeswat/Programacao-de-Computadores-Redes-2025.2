from logging import exception
import sys

lstValor    =       list()
intValor    =       1

while intValor != 0:
    try:
        intValor    =       int(input('Digite um valor: '))
    except ValueError:
        print('Digite um valor interio!')
    except exception is e:
        print (e)
    
    else:

        if intValor == 0:
            continue
        else:
            if intValor not in lstValor:
                lstValor.append(intValor)

print(f'{lstValor}')