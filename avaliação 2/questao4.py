'''Vamos desenvolver um programa que simula um terminal bancário contendo essas cinco operações:
Operações são suportadas:
D → realização de um depósito;
R → realização de uma retirada (saque);
C → pagamento de cheque emitido;
P → fazer um Pix para terceiro;
S → consulta de saldo;
Q → Sai do programa;'''

#Saldo inicial da conta.
saldo = 0.0

#Mensagem de boas vindas ao usuário
print('''\nBem vindo ao autoatendimento IFRN Bank, escolha uma das operações a seguir:

D → realização de um depósito
R → realização de uma retirada
C → pagamento de cheque emitido
P → fazer um Pix para terceiro
S → consulta de saldo
Q → Sai do programa''')

#loop principal do terminal.
while True:

#Solicita a operação desejada pelo usuário (entrada maiúscula ou minúscula)
    operação = input('\nSelecione a operação desejada (D/R/C/P/S/Q): ').strip().upper()

#Opção que sai do programa.
    if operação == 'Q':
        print('Obrigado por utilizar o IFRN Bank! Até logo! ')
        break

#Consulta de saldo.
    if operação == 'S':
        print(f'Saldo atual: R$ {saldo:.2f}')
        continue

#Operações que precisam de valores.
    if operação in ('D', 'R', 'C', 'P'):

#Mensagem personalizada para cada operação.
        if operação =='D':
            mens = ' Digite o valor do depósito (R$): '
        elif operação =='R':
            mens = ' Digite o valor do saque (R$): '
        elif operação == 'C':
            mens = ' Digite o valor do cheque (R$): '
        elif operação == 'P':
            mens = ' Digite o valor do PIX (R$): '

#Leitura da entrada e validação de número real positivo.
        try:
            valor = float(input(mens))
            if valor <=0:
                print('Erro: O valor deve ser positivo!')
                continue
        except ValueError:
            print(' Erro: Digite um numero válido!')
            continue

#Depósito
        if operação =='D':
            saldo += valor
            print(f' Depósito de R$ {valor:.2f} realizado com sucesso!')

#Saque
        elif operação =='R':
            if saldo >= valor:
               saldo -= valor
               print(f' Saque de R$ {valor:.2f} realizado com sucesso!')
            else:
               print(f' Saldo insuficiente! Saldo disponível: R$ {saldo:.2f}')

#Cheque
        elif operação =='C':
            if saldo >= valor:
                saldo -= valor
                print(f' Cheque de R$ {valor:.2f} compensado com sucesso!')
            else:
                print(f' Saldo insuficiente! Saldo disponível: R$ {saldo:.2f}')

#Pix
        elif operação == 'P':
            if saldo >= valor:
                saldo -= valor
                print(f' Pix de R$ {valor:.2f} enviado com sucesso!')
            else:
                print(f' Saldo insuficiente! Saldo disponível: R$ {saldo:.2f}')

#Operação inválida.
    else:
        print(' Operação inválida! use D, R, C, P, S ou Q. ')