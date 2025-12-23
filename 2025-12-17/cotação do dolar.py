'''
   Faça um programa que leia o arquivo "cotacao_dolar.csv" e em seguida gere
   dois arquivos: "cotacao_mes.csv" e "cotacao_ano.csv".

   O arquivo "cotacao_mes.csv" deve conter a cotação média do dólar para cada
   mês do ano (o usuário deve inicialmente informar o ano), no formato 
   "MM/AAAA,COTAÇÃO_MÉDIA".

   O arquivo "cotacao_ano.csv" deve conter a cotação média do dólar para cada
   ano presente no arquivo original, no formato "AAAA,COTAÇÃO_MÉDIA".
'''

import sys, os

strDiretorio = os.path.dirname(__file__)

strNomeArquivo = 'cotacao_dolar.csv'

try:

    arquiLeitura = open(f'{strDiretorio}/{strNomeArquivo}', 'r', encoding= 'utf-8')

except FileNotFoundError:
    sys.exit(f'Erro: Arquivo "{strNomeArquivo}" não encontrado')

except Exception as e:
    sys.exit(f'Erro: {e}')

else:

    lstListaGeral = list()

    while True:

        strLinha = arquiLeitura.readline().strip()

        if not strLinha: break

        lstDados = strLinha.split(';')

        lstData = lstDados[2].split('/')


        lstListaGeral.append(lstDados)

        print(lstData)
        
        
print(len(lstListaGeral))

arquiLeitura.close()