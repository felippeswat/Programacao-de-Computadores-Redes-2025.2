''' Vamos desenvolver um programa para calcular a área de um terreno a partir das 
medidas dos quatro lados e dois ângulos opostos fornecidos pelo usuário'''

# Bloco 1.
# Importando as bibliotecas necessárias.
import math
import sys

# Entrada de dados do usuário com tratamento de erro.
try:

    print('\nSeja bem vindo ao programa para cálculo de área da empresa DIATINF Engenharia!!! \n')
    print('Nosso programa é um dos mais modernos e avançados do mercado, pois facilitamos a utilizção e agilizamos o seu trabalho. \n')
    print('Para comprovar a facilidade do nosso programa vamos solicitar que você infome apenas as medidas em metros dos quatro lados do terreno e o valor em graus de dois ângulos opostos.\n')

    ladoa   =   float(input('Informe o valor do Lado A em metros: '))
    ladob   =   float(input('Informe o valor do Lado B em metros: '))
    ladoc   =   float(input('Informe o valor do Lado C em metros: '))
    ladod   =   float(input('Informe o valor do Lado D em metros: '))
    anguloa =   float(input('Informe o valor do ângulo α (alfa entre o lado A e B) em graus: '))
    anguloy =   float(input('Informe o valor do ângulo γ (gamma entre o lado C e D) em graus: '))

# Tratamento de erro pra valores não numéricos.
except ValueError:

    sys.exit('ERRO: Você deve digitar um valor numérico!')

# Tratamento para outros tipos de erro.
except Exception as strErro:
    
    sys.exit(f'ERRO: {strErro}')

else:

#Validando os dados para cerificar que formam um quadrilátero real.

# Bloco 2.
# Convertendo os ângulos de graus para raianos.
    aradianos   =   math.radians(anguloa)
    yradianos   =   math.radians(anguloy)

# Encontrando o cosseno dos ângulos.
    cosa        =   math.cos(aradianos)
    cosy        =   math.cos(yradianos)

# Bloco 3.
# Encontrando as diagonais.
    diagonal1   =   ((ladoa ** 2) + (ladob ** 2) - (2 * ladoa * ladob * cosa))
    diagonal2   =   ((ladoc ** 2) + (ladod ** 2) - (2 * ladoc * ladod * cosy))

# Validando as entradas para saber se formam um quadrilátero real.
if not math.isclose(diagonal1, diagonal2, rel_tol = 0.05):
    sys.exit('\n[ERRO], As medidas fornecidas são inconsistentes e não podem formar um quadrilatero real!')
    
else:
    print('\n[VALIDAÇÃO] Medidas consistentes, calculando área...\n')
# Bloco 4.
# Calculando o semiperímetro.
    semiperimetro       =   (ladoa + ladob + ladoc + ladod)/2

# Calculando a área do Terreno.
    area        =   math.sqrt((semiperimetro - ladoa) * (semiperimetro - ladob) * (semiperimetro - ladoc) * (semiperimetro - ladod) - (ladoa * ladob * ladoc * ladod) * (math.cos((aradianos + yradianos) / 2)) ** 2)

# Bloco 5.
# Imprimindo o valor da área do terreno formatada conforme solicitado.
print(f'A area do terreno é de {area:.2f} metros quadrados.')