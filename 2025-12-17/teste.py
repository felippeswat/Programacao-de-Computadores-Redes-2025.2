
import os

strDiretorio = os.path.dirname(__file__)

strNomeArquivo = 'capitais_brasil.csv'

# Abrir o arquivo para leitura ('r' de read)

arquiLeitura = open(f'{strDiretorio}/{strNomeArquivo}', 'r', encoding='utf-8')
    # Ler todas as linhas de uma vez e guardar numa lista
linhas = arquiLeitura.readlines()

# Mostrar as primeiras linhas pra ver se leu certo (pra teste)
print(linhas[:3])  # Mostra as 3 primeiras linhas

print(len(linhas))

arquiLeitura.close()