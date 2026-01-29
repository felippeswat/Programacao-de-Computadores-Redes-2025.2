


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
    
    dict_classificacao = dict(sorted(dict_times_filtrados.items(),key=lambda item: (item[1]['Pontuacao'], item[1]['Gols_Pro']),reverse=True))

    arq_escrita = open(f'{str_diretorio}/times_brasileirao_{int_ano}.json', 'w', encoding='utf-8')
    json.dump(dict_classificacao, arq_escrita, ensure_ascii=False, indent=4)
    arq_escrita.close

    #print(json.dumps(dict_times_filtrados, ensure_ascii=False, indent=4))