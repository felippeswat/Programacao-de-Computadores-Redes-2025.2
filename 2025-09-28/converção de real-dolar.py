print('Vamos converter valores em Reais para Dolar.')

reais       =float(input('Digite seu valor em Reais R$: '))
cotação     =float(input('Digite a cotação do dolar: '))

dolar       =reais/cotação

print(f'voçê tem: R$ {reais} na cotação de hoje de 1 dolar a R$ {cotação} você teria: $ {dolar:.2} dólares.')