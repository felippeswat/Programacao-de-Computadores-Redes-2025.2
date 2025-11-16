'''Vamos desenvolver um programa para compressão de uma entrada usando o algoritmo de compressão RLE!'''

#Pergunta qual a operação a realizar e valida a entrada em C ou D.
while True:
    operacao = input('Deseja comprimir ou descomprimir (C/D)? ').strip().upper()
    if operacao in ('C', 'D'):
        break
    print('Por favor digite apenas "C" ou "D".')

#Lê a entradad de dados do usuário e armazena limpando espaços no início e no final.
entrada = input('Digite a entrada para realizar a operação: ').strip()

#Início do bloco de compressão.
if operacao == 'C':

    resultado = ""
    i = 0
    tamanho = len(entrada)

    while i < tamanho:
        caractere = entrada[i]
        contador = 0

#Conta repetições seguidas.
        while i + contador < tamanho and entrada[i + contador] == caractere:

            contador += 1

#Divide em blocos de até 9.
        blocos = contador // 9
        resto = contador % 9

        for _ in range(blocos):
            resultado += "9" + caractere

        if resto > 0:
            resultado+= str(resto) + caractere

        i += contador

    print(f'Texto original: {entrada}')
    print(f'RLE: {resultado}')

#Início do bloco de descompressão.
else:
    resultado = ""
    i = 0
    tamanho = len(entrada)

    sucesso = True

    while i < tamanho and sucesso:

        num_str = ""

#Lê digitos do número.
        while i < tamanho and entrada[i].isdigit():
            num_str += entrada[i]
            i += 1

        if not num_str:
            print('A entrada deve conter numero! ')
            sucesso = False
            break
        
        numero = int(num_str)

#Valida numeros de 1 a 9.
        if numero < 1 or numero > 9:
            print(f'Número invállido {numero}, o numero deve ser entre 1 e 9! ')
            sucesso = False
            break
#Verifica se há letra após o número.
        if i >= tamanho:
            print('A entrada deve ter letra depois do numero! ')
            sucesso = False
            break
        
        caractere = entrada[i]
        i += 1

        resultado += caractere * numero

#Imprime o resultado se não houver erro ou uma mensagem caso um erro for encontrado.
    if sucesso:
        print(f'RLE : {entrada}')
        print(f'Descoprimida: {resultado}')

    else:
        print("Erro de entrada de dados, descompressão cancelada!")