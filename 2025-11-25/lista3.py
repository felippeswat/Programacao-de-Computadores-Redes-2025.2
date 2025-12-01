'''
   A partir da variável intQtValores, gere uma lista com a quantidade de valores 
   inteiros aleatórios entre 1 e 100, sem repetição. 
   
   Em seguida, o programa deve exibir:

   - A lista gerada
   - A soma dos valores na lista
   - A média dos valores na lista
   - O maior valor na lista
   - O menor valor na lista
   - A mediana dos valores na lista
   - A variância dos valores na lista
   - O desvio padrão dos valores na lista
'''

import random

intQtValores = 20
lstlista    =   list()
i = 0
mediana = 0

while i < intQtValores:

    x = random.randint(1, 100)
    if x not in lstlista:
        lstlista.append(x)
        i += 1

#função para somar os valores de uma lista
intsoma = sum(lstlista)

intmedia = intsoma/len(lstlista)

#Função para encontrar o maior valor de uma lista
intmaior = max(lstlista)

#Função para encontrar o menor valor de uma lista
intmenor = min(lstlista)

#Mediana
if len(lstlista) % 2 != 0:
    mediana = lstlista[len(lstlista) // 2]

else:
    mediana = (lstlista[len(lstlista) // 2 - 1] + lstlista[len(lstlista) // 2]) / 2

#Variância
fltvariancia = 0

for valor in lstlista:
    fltvariancia += (valor - intmedia) ** 2

fltvariancia /= len(lstlista)

#Desvio padrão

desvio = (fltvariancia ** 0.5)

print('A lista é: ')
print(lstlista)
print('A soma dos valores é: ')
print(intsoma)
print('A média dos valores é: ')
print(intmedia)
print('A mediana é: ')
print(mediana)
print('A variância é: ')
print(fltvariancia)
print('O desvio padrão é: ')
print(desvio)