print('Vamos converter temperatura entre suas escalas mais comuns.')
print('Vamos converter da escala celcius para a escala Fahrenheit.')

celsius       =float(input('Digite a temperatura em graus celcius ºc: '))

fahrenheit       =celsius*(9/5)+32 #Formulas para conversão de Celsius para Fahrenheit [( ºc*9/5)+32]

print(f'A temperatura de {celsius}ºC na escala Fahrenheit e igual a: {fahrenheit}ºF')