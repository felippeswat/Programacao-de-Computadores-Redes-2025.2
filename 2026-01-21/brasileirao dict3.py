


import sys, os ,json

str_diretorio = os.path.dirname(__file__)
str_aquivo = 'Times_Brasileirao.json'

try:

    arq_leitura = open(f'{str_diretorio}/{str_aquivo}', 'r', encoding='utf-8')

except FileNotFoundError:

    sys.exit(f'Arquivo {str_aquivo} não encontrado.')

except Exception as e:

    sys.exit(f'Erro ao abrir arquivo {str_aquivo}: {e}')

else:

    #dict_dados = json.dumps(json.load(arq_leitura), ensure_ascii=False)
    dict_dados = json.load(arq_leitura)
    arq_leitura.close

    #print(dict_dados)


    int_ano = 2025

    dict_times_filtrados = dict()

    for time, campanhas in dict_dados.items():
        for campanha in campanhas:
            if campanha['Ano'] == int_ano:

                dict_times_filtrados[time] = campanha
                break


    print(json.dumps(dict_times_filtrados, ensure_ascii=False, indent=4))