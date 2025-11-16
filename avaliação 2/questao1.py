'''vamos desenvolver um programa para encontrar quantos pares de números primos  (primos gêmeos) existem entre 2 e 1000000.'''

#Importando a biblioteca math
import math

numero = 100000
pares_gemeos    =   []

print(f'Procurando os primos gêmeos menores que {numero}...')

#Percorre os numeros ímpares do intervamo (do 3 ao 99997)
for menor in range(3, numero - 1, 2):
    
#Proximo impar consecutivo (+2)
    maior  =   menor + 2

#Assume que é primo até provar ao contrário
    e_primo_menor = True

#Testa de 2 ate raiz quadrada do menor e adicona +1 pra incluir.
    for d in range(2, int(math.sqrt(menor)) + 1):

#Se o resta do divizão for zero, não e primo.
        if menor % d == 0:
            e_primo_menor = False

#para o laço interno imediatamente.            
            break
    
#Se o menor não e primo, pula para o próximo sem testar o maior.    
    if not e_primo_menor:
        
#Vai para o próximo menor no laço principal.        
        continue


#Esse proximo bloco tem a mesma lógica macro do anterior, para testar o maior.
    e_primo_maior = True
    for d in range(2, int(math.sqrt(maior)) + 1):
        if maior % d == 0:
            e_primo_maior = False
            break

#Se os 2 forem true, esse bloco vai guardar o par na lista em tupla.
    if e_primo_maior:

        pares_gemeos.append((menor, maior))

#imprime a quantidade de pares primos consecutivos.
print(f'Total de primos gêmeos até {numero}: {len(pares_gemeos)}')

#impressão dos pares de primos comentada para verificação se necessário!
'''print('Pares encontrados: \n')
for par in pares_gemeos: 
    print(f'*({par[0]},{par[1]})')'''