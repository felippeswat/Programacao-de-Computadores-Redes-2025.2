# Vamos desenvolver um programa para calcular o valor total da permanência de um carro no estacionamento de acordo com a tabela de valores fornecida.

# Importando a biblioteca sys para tratamento de erros
import sys


# Entrada de dados do usuário com tratamento de erro
try:
    
    tempo = int(input('Informe o tempo de permanência no estacionamento (em Minutos): '))

# Tratamento de erro pra valores não numéricos
except ValueError:

    sys.exit('ERRO, você deve digitar uma valor numérico referente ao tempo de permanência em minutos!')

# Tratamento para outros tipos de erro
except Exception as strErro:

    sys.exit(f'ERRO: {strErro}')

else:

# Verificando se o valor da entrada é possitivo
    if tempo <= 0:
        sys.exit('ERRO, o valor deve ser positivo e maior que zero!')

# Tranformando o tempo fornecido para a exibição no formato solicitado
temp_horas   =   int(tempo//60)
temp_minutos =   int(tempo%60)

# Aredondamento da fração de hora para cobança
if tempo % 60 > 0:
    horas = int(temp_horas + 1)
else:
    horas   =   int(temp_horas)

# Imprimindo a quantidade do horas a serem cobradas
#print(f'horas a cobrar: {horas:02d}')(essa parte foi comentada pois não foi solicitado na resolução da questão, servindo apenas na hora do desenvolvimento do código)

# Calculando o valor total a ser cobrado
    # Calculando a primeira faixa de valores
if horas > 0 and horas <=2:
    total   =   horas*8

    # Calculando a segunda faixa de valores
elif horas > 2 and horas <= 4:
    total   =   16+(horas-2)*5

    # Calculando a terceira faixa de valores
elif horas > 4 and horas < 6:
    total   =   26+(horas-4)*3

    # Valor fixo da ultima faixa de valores
else:
    total   =   30

# Imprimindo o tempo de parmanências no formato solicitado
print(f'O tempo de permanência no estacionamento foi de: {temp_horas:02d}:{temp_minutos:02d}')

# Imprimindo o valor total no formato solicitado
if horas == 1:
    print(f'O valor total é de: R$ {total:.2f} reais, referente a: {horas:02d} hora')

else:
    print(f'O valor total é de: R$ {total:.2f} reais, referente a: {horas:02d} horas')