

import os, sys, json

str_diretorio = os.path.dirname(__file__)
str_nome_arquivo = f'{str_diretorio}/Brasileirao_Serie_A.csv'

try:

    arq_entrada = open(str_nome_arquivo, 'r', encoding='utf-8')

except FileNotFoundError:
    sys.exit('Erro: Arquivo não encontrado!')

except Exception as e:
    sys.exit(f'Erro ao abrir arquivo: {e}')

else:

    lst_chaves = arq_entrada.readline().strip().split(';')

    lst_chaves.pop(0)

    dict_times = dict()

    while True:

        str_linha = arq_entrada.readline().strip()

        if not str_linha:
            break

        lst_dados = str_linha.split(';')

        str_time = lst_dados[0]

        lst_dados.pop(0)

        dict_info_ano = dict(zip(lst_chaves, lst_dados))

        for str_chave in dict_info_ano.keys():
            if dict_info_ano[str_chave].isdigit():
                dict_info_ano[str_chave] = int(dict_info_ano[str_chave])

        dict_info_ano['Pontuacao'] = dict_info_ano['Vitorias'] * 3 + dict_info_ano['Empates']

        dict_info_ano['Saldo_Gols'] = dict_info_ano['Gols_Pro'] - dict_info_ano['Gols_Contra']


        if not str_time in dict_times.keys():

            dict_times[str_time] = [dict_info_ano]

        else:

            dict_times[str_time].append(dict_info_ano)


    arq_entrada.close()

    dict_times = json.dumps(dict_times, ensure_ascii=False)

    str_nome_arquivo_saida = f'{str_diretorio}/Times_Brasileirao.json'

    try:

        arq_saida = open(str_nome_arquivo_saida, 'w', encoding='utf-8')

    except Exception as e:
        sys.exit(f'Erro ao salvar aquivo JSON. {e}')
    
    else:

        arq_saida.write(dict_times)
        arq_saida.close()