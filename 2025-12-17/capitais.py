
'''Fazer um programa que leia o arquivo capitais_brasil.csv e
   preencha uma lista com sublistas contendo o nome da capital, 
   a sigla do seu estado, a sigla da sua região e a sua população.

   Após gerar a lista, gere uma lista contendo a sigla da região
   e o total da população das capitais daquela região.

   Em seguida salve o resultado em um arquivo chamado populacao_regioes.csv,
   no mesmo diretório onde se encontra o programa, no seguinte formato 
   (os valores abaixo são apenas ilustrativos):

   Região;População
   N;123456
   NE;234567
   CO;345678
   S;456789
   SE;567890
   
   Não use bibliotecas para manipulação de arquivos CSV.
   Usar set() e usar filter()'''

import sys, os

strDiretorio = os.path.dirname(__file__)

strNomeArquivo = 'capitais_brasil.csv'

try:

    arquiLeitura = open(f'{strDiretorio}/{strNomeArquivo}', 'r', encoding= 'utf-8')

except FileNotFoundError:
    sys.exit(f'Erro: Arquivo "{strNomeArquivo}" não encontrado')

except Exception as e:
    sys.exit(f'Erro: {e}')

else:

    listaGeral = list()

    while True:

        strLinha = arquiLeitura.readline()

        if not strLinha: break

        print(strLinha)

for linha in strLinha:

    strCapital = linha[0].strip()
    strUf      = linha[1].strip()
    strRegiao  = linha[2].strip()
    strPop     = linha[3].strip()

    listaGeral.append([strCapital, strUf, strRegiao, strPop])

    print(strCapital)
    print(strUf)
    print(strRegiao)
    print(strPop)
    #print(listaGeral)

arquiLeitura.close()
