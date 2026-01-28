

import os, sys, json

str_diretorio = os.path.dirname(__file__)
str_nome_arquivo = f'{str_diretorio}\Brasileirao_Serie_A.csv'

try:

    arq_entrada = open(str_nome_arquivo, 'r', encoding='utf-8')

except FileNotFoundError:
    sys.exit('Erro: Arquivo não encontrado!')

except Exception as e:
    sys.exit(f'Erro ao abrir aqrquivo: {e}')

else:

    lst_chaves = arq_entrada.readline().strip().split(';')

    lst_chaves.pop(0)

    dict_classificacao = dict()

    while True:

        str_linha = arq_entrada.readline().strip()

        if not str_linha:
            break

        lst_dados = str_linha.split(';')

        str_time = lst_dados[0]

        lst_dados.pop(0)

        dict_time = dict(zip(lst_chaves, lst_dados))

        dict_classificacao[str_time] = dict_time

    arq_entrada.close()

    dict_classificacao = json.dumps(dict_classificacao, ensure_ascii=False)

    print(dict_classificacao)