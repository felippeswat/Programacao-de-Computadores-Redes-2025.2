# Vamos desenvolver um programa para calcular o imposto de renda retino na fonte.

# Importando a biblioteca sys para tratamento de erros.
import sys

# Entrada de dados do usuário com tratamento de erro.
try:

    salario     =   float(input('Informe o valor da sálaio bruto: '))
    inss        =   float(input('Informe o valor referente ao INSS: '))
    dependentes =   int(input('Informe o numero de dependentes (caso não haja dependentes digite 0 "zero"): '))

# Tratamento de erro pra valores não numéricos
except ValueError:

    sys.exit('ERRO: Você deve digitar um valor numérico!')

# Tratamento para outros tipos de erro
except Exception as strErro:

    sys.exit(f'ERRO: {strErro}')

else:

# Verificando se o valor da entrada é possitivo
    if salario <= 0:
        sys.exit('ERRO, o valor do salário deve ser positivo e maior que zero!')
    
    elif inss <= 0:
        sys.exit('ERRO, o valor do INSS deve ser positivo e maior que zero!')

    elif dependentes < 0:
        sys.exit('ERRO, o numero de dependentes não pode ser negativo!')

# Encontrando o valor da Base de Cálculo (BC).
bc  =   salario - inss - (dependentes*189.59)

# Imprimindo Salario, INSS, numero de dependentes e a base de cálculo.
#print(f'salario: {salario:.2f}, INSS: {inss:.2f}, Dependentes: {dependentes}, Base de cálculo: {bc:.2f}')(essa parte foi comentada pois não foi solicitado na resolução da questão, servindo apenas na hora do desenvolvimento do código)

if bc   <=  2428.80:
    sys.exit('Contribuinte se enquadra na fixa de isenção!')

elif bc > 2428.80 and bc <= 2826.65:
    aliquota    =   float(0.075)
    deducao     =   float(182.16)

elif bc > 2826.65 and bc <= 3751.05:
    aliquota    =   float(0.15)
    deducao     =   float(394.16)

elif bc > 3751.05 and bc <= 4664.68:
    aliquota    =   float(0.225)
    deducao     =   float(675.49)

else:
    aliquota    =   float(0.275)
    deducao     =   float(908.73)

# Imprimindo a faixa de alíquota e a faixa de dedução.
#print(f'Alíquota de acordo com a faixa da tabela: {aliquota*100:.2f}%')(essa parte foi comentada pois não foi solicitado na resolução da questão, servindo apenas na hora do desenvolvimento do código)
#print(f'Dedução de acordo com a faixa da tabela: R$ {deducao:.2f}')(essa parte foi comentada pois não foi solicitado na resolução da questão, servindo apenas na hora do desenvolvimento do código)

# Calculando o valor do IRRF.
irrf    =   float(bc * aliquota)-deducao

# Verificando se o valor do importo devido é negativo ou não e imprimindo o valor do IRRF.
if irrf <= 0:
    irrf    =   float(0.00)
    print(f'O valor do imposto devido é: R$ {irrf:.2f}')

else:
    print(f'O valor do imposto devido é: R$ {irrf:.2f}')