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

while i < lstlista:
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

print('A lista é: ')
print(lstlista)
print('A soma dos valores é: ')
print(intsoma)

