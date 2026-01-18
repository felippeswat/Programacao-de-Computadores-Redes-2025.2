#20252014050025:Felippe José Ferreira de Góes Mariano

'''Questão 3 - Análise de Log do Apache, Uso de filter(), map(), sorted(), lambda para análise'''
import sys
import os

strDiretorio = os.path.dirname(__file__)
strArquivo = 'apache.log'

# Listas para armazenar os dados brutos (tuplas)
lstIps = []           # [(ip, 1), (ip, 1), ...]
lstDiasTotal = []     # [("Nov 29 2005", 1), ...]
lstDiasErro = []      # [("Jul 21 2005", 1), ...]

try:
    arq = open(f'{strDiretorio}/{strArquivo}', 'r', encoding='utf-8')
    
    while True:

        linha = arq.readline().rstrip()
        if not linha:
            break
        
        if '[client' not in linha:
            continue
        
        partes = linha.split()
        if len(partes) < 10:
            continue
        
        # Extrai IP
        idx_client = partes.index('[client')
        ip = partes[idx_client + 1].rstrip(']')
        
        # Extrai data
        mes = partes[1]
        dia = partes[2]
        ano = partes[4]
        chave_dia = f"{mes} {dia} {ano}"
        
        # Adiciona em todas as listas (contagem de 1 por ocorrência)
        lstIps.append((ip, 1))
        lstDiasTotal.append((chave_dia, 1))
        
        # Verifica se é erro forbidden/denied
        linha_lower = linha.lower()
        if 'forbidden' in linha_lower or 'denied' in linha_lower or 'directory index forbidden' in linha_lower:
            lstDiasErro.append((chave_dia, 1))
    
    arq.close()

except Exception as e:
    print(f'Erro ao ler o arquivo: {e}')
    sys.exit(1)

# Função auxiliar para somar ocorrências iguais (usando filter e map)
def contar_ocorrencias(lista_tuplas):
    if not lista_tuplas:
        return []
    
    # Pega todos os valores únicos (usando set)
    valores_unicos = set(map(lambda x: x[0], lista_tuplas))
    
    # Para cada valor único, conta quantas vezes aparece
    contagens = []
    for valor in valores_unicos:
        ocorrencias = len(list(filter(lambda x: x[0] == valor, lista_tuplas)))
        contagens.append((valor, ocorrencias))
    
    return contagens

# 1. Contagem por IP
ips_contados = contar_ocorrencias(lstIps)
ips_ordenados = sorted(ips_contados, key=lambda x: x[1], reverse=True)
top_ip = ips_ordenados[0] if ips_ordenados else ('Nenhum', 0)

# 2. Contagem total por dia
dias_total_contados = contar_ocorrencias(lstDiasTotal)
dias_total_ordenados = sorted(dias_total_contados, key=lambda x: x[1], reverse=True)
dia_pico = dias_total_ordenados[0] if dias_total_ordenados else ('Nenhum', 0)

# 3. Contagem de erros por dia
dias_erro_contados = contar_ocorrencias(lstDiasErro)
dias_erro_ordenados = sorted(dias_erro_contados, key=lambda x: x[1], reverse=True)
dia_critico = dias_erro_ordenados[0] if dias_erro_ordenados else ('Nenhum', 0)

# Resultados finais
print('\n' + '='*70)
print('RESULTADOS DA ANÁLISE DO LOG APACHE')
print(f'1. IP mais frequente: {top_ip[0]} ({top_ip[1]} ocorrências)')
print(f'2. Dia com mais Tráfego: {dia_pico[0]} ({dia_pico[1]} ocorrências)')
print(f'3. Dia com mais erros: {dia_critico[0]} ({dia_critico[1]} ocorrências)')
print('='*70)