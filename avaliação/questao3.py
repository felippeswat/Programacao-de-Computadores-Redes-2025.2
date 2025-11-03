# Vamos desenvolver um programa para trabalhar como um computador de bordo.

# Importando a biblioteca sys para tratamento de erros.
import sys

# Entrada de dados do usuário com tratamento de erro.
try:

    hpartida     =   int(input('Informe a hora da partida: '))
    mpartida     =   int(input('Informe o minuto da partida: '))
    hchegada     =   int(input('Informe a hora da chegada: '))
    mchegada     =   int(input('Informe o minuto da chegada: '))
    descanso     =   int(input('Informe o tempo total de paradas para descanso e alimentação em minutos: '))
    combustivel  =   float(input('Informe a quantidade total de litros de combustivel gasto na viagem: '))
    preçolitro   =   float(input('Informe o preço do litro de combustivel: '))
    distancia    =   float(input('Informe a distância total percorrida (em Km): '))


# Tratamento de erro pra valores não numéricos
except ValueError:

    sys.exit('ERRO: Você deve digitar um valor numérico!')

# Tratamento para outros tipos de erro
except Exception as strErro:
    
    sys.exit(f'ERRO: {strErro}')

else:

# Verificando se o valor da entrada é possitivo
    if hpartida < 0 and hpartida > 23:
        sys.exit('ERRO, a hora da partida deve ser entre 0 e 23 horas!')
    
    elif mpartida < 0 and mpartida > 59:
        sys.exit('ERRO, o minuto da partda deve ser entre 0 e 59 minutos!')

    elif hchegada < 0 and hchegada > 23:
        sys.exit('ERRO, a hora da chegada deve ser entre 0 e 23 horas!')

    elif mchegada < 0 and mchegada > 59:
        sys.exit('ERRO, o minuto da partda deve ser entre 0 e 59 minutos!')

    elif descanso < 0:
        sys.exit('ERRO, o valor deve ser positivo!')

    elif combustivel < 0:
        sys.exit('ERRO, o valor deve ser positivo!')

    elif preçolitro < 0:
        sys.exit('ERRO, o valor deve ser positivo!')

    elif distancia < 0:
        sys.exit('ERRO, o valor deve ser positivo!')

# Convertendo as variaveis de tempo todas para minutos
partidaminutos   =   (hpartida*60) + mpartida
chegadaminutos   =   (hchegada*60) + mchegada

# Calculando tempo total de viagem e formatndo para impressão conforme solicitado
tempototal          =   (chegadaminutos - partidaminutos)
tempototalhoras     =   (tempototal) // 60
tempototalminutos   =   (tempototal) % 60

# Calculando tempo em movimento
tempoemmovimento    =   tempototal - descanso

# Calculando a velocidade média global e velocidade média em movimento.
velocidademediaglobal           =   distancia/(tempototal / 60)
velocidademediaemmovimento      =   distancia/(tempoemmovimento / 60)

# Calculando o custo total da viagem.
custototal      =   combustivel * preçolitro

# Calculando o desempenho do carro (Km por Litro).
desempenho       =   distancia/combustivel

# Calculando o comsumo em (litros por Hora).
consumo         =   combustivel/(tempoemmovimento / 60)

# Calculando o custo por Kilomentro (R$ por Km).
custoporkm      =   custototal/distancia

# Formatando a impressão do relatório da viagem como solicitado.
print(f'--- Relatório da Viagem --- \n\nResultados Gerais: \n   - Tempo Total de Viagem: {tempototalhoras}:{tempototalminutos} \n   - Custo total com Combustível: {custototal:.2f}\n')

print(f'Velocidade: \n   - Velocidade Média Global: {velocidademediaglobal:.2f} Km/h \n   - Velocidade Média em Movimento: {velocidademediaemmovimento:.2f} Km/h \n')

print(f'Desempenho do Veículo: \n   - Consumo (Km/l): {desempenho:.2f} Km/l \n   - Consumo (l/h): {consumo:.2f} l/h \n   - Custo por Distância (R$/Km): {custoporkm:.2f} \n')

