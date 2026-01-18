#20252014050025:Felippe José Ferreira de Góes Mariano;


'''Questão 1 - Brasileirão Série A, Leitura do arquivo, cálculo de pontos e saldo de gols'''

import sys
import os

# Pegando o diretório onde está o programa
strDiretorio = os.path.dirname(__file__)

# Nome do arquivo de entrada (conforme você informou)
strNomeArquivo = 'Basileirao_Serie_A.csv'

# Lista principal que vai guardar todos os dados
lstTimes = []

try:
    # Abrindo o arquivo para leitura
    arquiLeitura = open(f'{strDiretorio}/{strNomeArquivo}', 'r', encoding='utf-8')
    
    # Lendo a primeira linha (cabeçalho) e descartando
    strCabecalho = arquiLeitura.readline().strip()
    #print('Cabeçalho encontrado:', strCabecalho)
    
    while True:
        strLinha = arquiLeitura.readline().strip()
        
        
        if not strLinha:
            break
            
        # Separando os campos pelo ;
        lstDados = strLinha.split(';')
        
        # Verificando se tem a quantidade certa de colunas
        if len(lstDados) != 9:
            print(f'Linha ignorada (número de campos errado): {strLinha}')
            continue

        # Convertendo os campos numéricos
        try:
            strTime          = lstDados[0].strip()
            strAno           = lstDados[1].strip()
            intVitorias      = int(lstDados[2].strip())
            intEmpates       = int(lstDados[3].strip())
            intDerrotas      = int(lstDados[4].strip())
            intGolsPro       = int(lstDados[5].strip())
            intGolsContra    = int(lstDados[6].strip())
            intAmarelos      = int(lstDados[7].strip())
            intVermelhos     = int(lstDados[8].strip())
            
            # Calculando os valores pedidos
            intPontos = (intVitorias * 3) + intEmpates
            intSaldo  = intGolsPro - intGolsContra
            
            # Criando a linha completa com os novos campos na ordem solicitada
            lstLinhaCompleta = [
                strTime,
                strAno,
                intVitorias,
                intEmpates,
                intDerrotas,
                intPontos,         
                intGolsPro,
                intGolsContra,
                intSaldo,          
                intAmarelos,
                intVermelhos
            ]
            
            lstTimes.append(lstLinhaCompleta)
            
        except ValueError as erroConversao:
            print(f'Erro de conversão na linha: {strLinha}')
            print(f'Detalhe: {erroConversao}')
            continue

    arquiLeitura.close()
    
    print('\nLeitura concluída com sucesso!')
    print(f'Total de linhas válidas lidas: {len(lstTimes)}')
    #print('Primeiras 3 linhas (exemplo):')
    #for i in range(min(3, len(lstTimes))):
        #print(lstTimes[i])

    # -----------------------------
    # PARTE 2: Encontrar anos únicos e mostrar progresso
    # -----------------------------

    print('\n' + '='*50)
    print('PARTE 2: Anos encontrados nos dados')

    # Usando set() para pegar anos únicos (seu estilo preferido!)
    anos_unicos = set()

    for time in lstTimes:
        anos_unicos.add(time[1])  # time[1] é o Ano (posição 1 na lista)

    # Convertendo para lista e ordenando (pra ficar bonito)
    lstAnos = sorted(list(anos_unicos))

    print(f'Anos encontrados: {len(lstAnos)}')
    print('Anos disponíveis:', lstAnos)

    # Exemplo de quantos times por ano (só pra depuração, pode remover depois)
    for ano in lstAnos:
        # Filtrando com filter + lambda (como no seu exemplo de capitais)
        times_do_ano = list(filter(lambda t: t[1] == ano, lstTimes))
        print(f'{ano}: {len(times_do_ano)} times')

    print('\n' + '='*50)
    print('PARTE 3: Gerando arquivos de classificação por ano...')

    arquivos_criados = []  # vamos guardar os nomes dos arquivos gerados

    for ano in lstAnos:
        
        # Filtrar times daquele ano (usando filter + lambda, seu estilo)
        times_do_ano = list(filter(lambda t: t[1] == ano, lstTimes))
        
        if not times_do_ano:
            print(f'Ano {ano}: Nenhum time encontrado (pulando)')
            continue
        
        # Ordenação múltipla (critérios do enunciado, em ordem de prioridade):
        # 1. Pontos (maior) → índice 5, descendente
        # 2. Vitórias (maior) → índice 2, descendente
        # 3. Saldo de gols (maior) → índice 8, descendente
        # 4. Gols Pró (maior) → índice 6, descendente
        times_ordenados = sorted(
            times_do_ano,
            key=lambda t: (-t[5], -t[2], -t[8], -t[6]),  # negativos = descendente
            reverse=False
        )
        
        # Nome do arquivo de saída
        nome_arquivo_saida = f'brasileirao_{ano}.csv'
        caminho_saida = f'{strDiretorio}/{nome_arquivo_saida}'
        
        try:
            arquiSaida = open(caminho_saida, 'w', encoding='utf-8')
            
            # Escrevendo o cabeçalho (exatamente como pedido)
            arquiSaida.write(
                "Time;Ano;Vitórias;Empates;Derrotas;Pontos;Gols Pró;Gols Contra;Saldo;Cartões Amarelos;Cartões Vermelhos\n"
            )
            
            # Escrevendo os times ordenados
            for time in times_ordenados:
                linha_csv = ';'.join(str(valor) for valor in time)
                arquiSaida.write(linha_csv + '\n')
            
            arquiSaida.close()
            
            arquivos_criados.append(nome_arquivo_saida)
            print(f'Arquivo gerado com sucesso: {nome_arquivo_saida} ({len(times_ordenados)} times)')
            
        except Exception as e:
            print(f'Erro ao gerar arquivo {nome_arquivo_saida}: {e}')

    # Resumo final da geração
    print('\nGeração concluída!')
    if arquivos_criados:
        print('Arquivos criados:')
        for arq in arquivos_criados:
            print(f'  - {arq}')
    else:
        print('Nenhum arquivo foi gerado (verifique os dados)')

    print('\n' + '='*50)
    print('PARTE 4: Exibição interativa da classificação')
    print('Arquivos gerados com sucesso (já listados acima)')

    # Mostrando novamente os anos disponíveis (pra ajudar o usuário)
    print('Anos disponíveis para consulta:', lstAnos)

    while True:
        try:
            strAnoDesejado = input('\nDigite o ano que deseja ver a classificação (ou "sair" para finalizar): ').strip()
        
            if strAnoDesejado.lower() == 'sair':
                print('Programa finalizado!')
                break
        
            if strAnoDesejado not in lstAnos:
                print(f'Ano {strAnoDesejado} não encontrado. Tente novamente.')
                continue
        
            # Filtrando e ordenando novamente (pra mostrar na tela)
            times_do_ano = list(filter(lambda t: t[1] == strAnoDesejado, lstTimes))
            times_ordenados = sorted(
                times_do_ano,
                key=lambda t: (-t[5], -t[2], -t[8], -t[6])
            )

        except KeyboardInterrupt:
            print('\nPrograma interrompido pelo usuário. Boa sorte na entrega!')
            break
        except Exception as e:
            print(f'Ops... algo deu errado: {e}. Tente novamente.')
        
        print(f'\nClassificação do Brasileirão {strAnoDesejado} (20 times):')
        print('-'*70)
        print(f"{'Pos':<4} {'Time':<25} {'Pts':<5} {'V':<4} {'E':<4} {'D':<4} {'SG':<5} {'GP':<5}")
        print('-'*70)
        
        for pos, time in enumerate(times_ordenados, 1):
            print(f"{pos:<4} {time[0]:<25} {time[5]:<5} {time[2]:<4} {time[3]:<4} {time[4]:<4} {time[8]:<5} {time[6]:<5}")
        
        # -----------------------------
        # PARTE 7: Estatísticas gerais do ano escolhido
        # -----------------------------
        
        print('\nEstatísticas do ano ' + strAnoDesejado + ':')
        
        # 7.1 Time(s) com mais cartões amarelos
        max_amarelos = max(t[9] for t in times_ordenados)
        times_max_amarelos = [t[0] for t in times_ordenados if t[9] == max_amarelos]
        print(f"Time(s) com mais amarelos ({max_amarelos}): {', '.join(times_max_amarelos)}")
        
        # 7.2 Time(s) com mais cartões vermelhos
        max_vermelhos = max(t[10] for t in times_ordenados)
        times_max_vermelhos = [t[0] for t in times_ordenados if t[10] == max_vermelhos]
        print(f"Time(s) com mais vermelhos ({max_vermelhos}): {', '.join(times_max_vermelhos)}")
        
        # 7.3 Time(s) que mais fizeram gols (Gols Pró)
        max_gols_pro = max(t[6] for t in times_ordenados)
        times_max_gols_pro = [t[0] for t in times_ordenados if t[6] == max_gols_pro]
        print(f"Time(s) que mais fizeram gols ({max_gols_pro}): {', '.join(times_max_gols_pro)}")
        
        # 7.4 Time(s) que mais sofreram gols (Gols Contra)
        max_gols_contra = max(t[7] for t in times_ordenados)
        times_max_gols_contra = [t[0] for t in times_ordenados if t[7] == max_gols_contra]
        print(f"Time(s) que mais sofreram gols ({max_gols_contra}): {', '.join(times_max_gols_contra)}")
    
except FileNotFoundError:
    sys.exit(f'ERRO: Arquivo "{strNomeArquivo}" não encontrado no diretório {strDiretorio}')
    
except Exception as e:
    sys.exit(f'ERRO inesperado durante a leitura: {e}')