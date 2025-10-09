'''
	Crie um programa em Python que calcule as raízes de uma equação do 2º grau.
	
	O programa deve:
	
		- Ler os valores de a, b e c como entrada;
		
		- Verificar se o valor de a é zero. Caso seja, a equação não será do 
		  2º grau e o programa deve informar o usuário sobre isso e encerrar;
		  
		- Calcular o discriminante (delta) e, com base no valor de delta:
			
			- delta > 0 : a equação possui duas raízes reais distintas. 
			  O programa deve calcular e exibir ambas as raízes;
			  
			- delta = 0 : a equação possui uma única raiz real. 
			  O programa deve calcular e exibir a raiz única;
			  
			- delta < 0 : a equação não possui raízes reais. 
			  O programa deve informar ao usuário que não existem raízes reais.		
'''
from re import A, X
import sys


print('Vamos calcular o valor das raizes da equação de 2º grau')

a       =int(input('Informe o valor de "a" na equação: '))

if (a == 0):
    sys.exit('Valor de "a" é zero, com isso a equção não é de 2º grau!')

b       =int(input('Informe o valor de "b" na equação: '))
c       =int(input('Informe o valor de "c" na equação: '))

#print(f'a: {a}')
#print(f'b: {b}')
#print(f'c: {c}')


delta     =(b**2)-4*a*c

print(f'O valor de Delta é: {delta}')

if (delta > 0):
    x1      = -b+(delta**(1/2))/(2*a)
    x2      = -b-(delta**(1/2))/(2*a)

    print(f'A equação possui 2 raizes e são elas: X1={x1:.2f} e X2={x2:.2f}')

elif (delta == 0):
    x       = -b/(2*a)

    print(f'A equação possui 1 raiz X={x:.2f}')

else:
	
	print('A equação não possui raizes reais')