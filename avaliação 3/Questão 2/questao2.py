#20252014050025:Felippe José Ferreira de Góes Mariano

'''Questão 2 - Mega Sena, Leitura de resultados, geração de aposta, filtro de acertos e probabilidades'''

import sys
import os
import random
from math import comb  # Para calcular combinações nas probabilidades

# Pegando o diretório onde está o programa
strDiretorio = os.path.dirname(__file__)

# Nome do arquivo de entrada
strNomeArquivo = 'Resultados_Mega_Sena.csv'

# Lista principal que vai guardar todos os concursos (lista de listas)
lstConcursos = []

try:
    # Abrindo o arquivo para leitura
    arquiLeitura = open(f'{strDiretorio}/{strNomeArquivo}', 'r', encoding='utf-8')
    
    # Lendo e guardando o cabeçalho (pra usar nos arquivos de saída)
    strCabecalho = arquiLeitura.readline().strip()
    print('Cabeçalho encontrado:', strCabecalho)

    while True:
        strLinha = arquiLeitura.readline().strip()
        
        # Se chegou no final do arquivo, para
        if not strLinha:
            break
            
        # Separando os campos pelo ;
        lstDados = strLinha.split(';')
        
        # Verificando se tem a quantidade certa de colunas (8: concurso + data + 6 bolas)
        if len(lstDados) != 8:
            print(f'Linha ignorada (número de campos errado): {strLinha}')
            continue

        # Convertendo os campos numéricos (bolas para int, concurso e data ficam str)
        try:
            strConcurso = lstDados[0].strip()
            strData     = lstDados[1].strip()
            intBola1    = int(lstDados[2].strip())
            intBola2    = int(lstDados[3].strip())
            intBola3    = int(lstDados[4].strip())
            intBola4    = int(lstDados[5].strip())
            intBola5    = int(lstDados[6].strip())
            intBola6    = int(lstDados[7].strip())
            
            # Criando a sublista completa do concurso
            lstConcursoCompleto = [
                strConcurso,
                strData,
                intBola1,
                intBola2,
                intBola3,
                intBola4,
                intBola5,
                intBola6
            ]
            
            lstConcursos.append(lstConcursoCompleto)
            
        except ValueError as erroConversao:
            print(f'Erro de conversão na linha: {strLinha}')
            print(f'Detalhe: {erroConversao}')
            continue

    arquiLeitura.close()

    print('\nLeitura concluída com sucesso!')
    print(f'Total de concursos lidos: {len(lstConcursos)}')
    print('Primeiros 3 concursos (exemplo):')
    for i in range(min(3, len(lstConcursos))):
        print(lstConcursos[i])

except FileNotFoundError:
    sys.exit(f'ERRO: Arquivo "{strNomeArquivo}" não encontrado no diretório {strDiretorio}')
    
except Exception as e:
    sys.exit(f'ERRO inesperado durante a leitura: {e}')

# 1. Solicitar quantidade de dezenas ao usuário (6 a 20)
while True:
    try:
        intQtdDezenas = int(input('\nDigite um valor entre 6 e 20 para a quantidade de dezenas: '))
        if 6 <= intQtdDezenas <= 20:
            break
        else:
            print('Valor inválido! Deve ser entre 6 e 20.')
    except ValueError:
        print('Por favor, digite um número inteiro válido.')

# 2. Gerar aposta aleatória (dezenas únicas entre 1 e 60)
lstAposta = sorted(random.sample(range(1, 61), intQtdDezenas))
print(f'\nAposta gerada aleatoriamente ({intQtdDezenas} dezenas): {lstAposta}')

# 3. Gerar as 3 listas filtradas (sena=6 acertos, quina=5, quadra=4)
lstSena = []
lstQuina = []
lstQuadra = []

for lstConcurso in lstConcursos:
    # Pegando só as 6 dezenas do concurso (posições 2 a 7)
    setDezenasSorteadas = set(lstConcurso[2:])
    
    # Pegando acertos (interseção de sets, rápido e sem repetições)
    setAcertos = set(lstAposta) & setDezenasSorteadas
    intAcertos = len(setAcertos)
    
    if intAcertos == 6:
        lstSena.append(lstConcurso)
    elif intAcertos == 5:
        lstQuina.append(lstConcurso)
    elif intAcertos == 4:
        lstQuadra.append(lstConcurso)

print('\nFiltragem concluída!')
print(f'Resultados encontrados: Sena={len(lstSena)}, Quina={len(lstQuina)}, Quadra={len(lstQuadra)}')

# 4. Salvar as listas em arquivos separados (com cabeçalho e mesmo formato)
def salvar_lista_arquivo(strNomeArq, lstDados):
    try:
        arquiSaida = open(f'{strDiretorio}/{strNomeArq}', 'w', encoding='utf-8')
        
        # Escrevendo o cabeçalho
        arquiSaida.write(strCabecalho + '\n')
        
        # Escrevendo os dados
        for lstLinha in lstDados:
            strLinhaCsv = ';'.join(str(valor).strip() for valor in lstLinha)
            arquiSaida.write(strLinhaCsv + '\n')
        
        arquiSaida.close()
        print(f'Arquivo gerado com sucesso: {strNomeArq} ({len(lstDados)} resultados)')
    
    except Exception as e:
        print(f'Erro ao gerar arquivo {strNomeArq}: {e}')

salvar_lista_arquivo('resultados_sena.csv', lstSena)
salvar_lista_arquivo('resultados_quina.csv', lstQuina)
salvar_lista_arquivo('resultados_quadra.csv', lstQuadra)

# 5. Exibir quantidades (já fizemos acima, mas repetindo pra clareza)
print('\nResumo de resultados obtidos:')
print(f' - Sena (6 acertos): {len(lstSena)} sorteios')
print(f' - Quina (5 acertos): {len(lstQuina)} sorteios')
print(f' - Quadra (4 acertos): {len(lstQuadra)} sorteios')

# 6. Calcular probabilidades teóricas (para exatos 4,5,6 acertos)
print(f'\nProbabilidades teóricas com {intQtdDezenas} dezenas (1 em X chances):')

# Fórmula: probabilidade de exatos m acertos = comb(6,m) * comb(54, k-m) / comb(60,k)
try:
    total_combs = comb(60, intQtdDezenas)

    # Sena (6 acertos)
    if intQtdDezenas >= 6:
        comb_sena = comb(6, 6) * comb(54, intQtdDezenas - 6)
        prob_sena = comb_sena / total_combs if total_combs > 0 else 0
        print(f'Sena: 1 em {total_combs / comb_sena:.0f}' if comb_sena > 0 else 'Sena: Impossível (muitos acertos)')
    else:
        print('Sena: Impossível (menos de 6 dezenas)')
    
    # Quina (5 acertos)
    if intQtdDezenas >= 5:
        comb_quina = comb(6, 5) * comb(54, intQtdDezenas - 5)
        prob_quina = comb_quina / total_combs if total_combs > 0 else 0
        print(f'Quina: 1 em {total_combs / comb_quina:.0f}' if comb_quina > 0 else 'Quina: Impossível')
    else:
        print('Quina: Impossível (menos de 5 dezenas)')
    
    # Quadra (4 acertos)
    if intQtdDezenas >= 4:
        comb_quadra = comb(6, 4) * comb(54, intQtdDezenas - 4)
        prob_quadra = comb_quadra / total_combs if total_combs > 0 else 0
        print(f'Quadra: 1 em {total_combs / comb_quadra:.0f}' if comb_quadra > 0 else 'Quadra: Impossível')
    else:
        print('Quadra: Impossível (menos de 4 dezenas)')

except ValueError:
    print('Erro no cálculo de probabilidades (valor inválido para combinações).')

print('\nPrograma concluído!')