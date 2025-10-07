print('Vamos calcular a conta do restaurante incluindo a gorjeta.')

conta       =float(input('Digite o valor da conta: '))
percentual  =float(input('Digite o valor em percenual que deja deixar de gorjeta para o garçon: '))

gorjeta     =conta*(percentual/100)
total       =conta+gorjeta


print(f'O valor total é de:  R$ {total}, sendo que R$ {conta} é referente ao consummo e R$ {gorjeta} de gorjeta.')