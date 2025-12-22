# Importar nada! Usamos só Python puro.

# Abrir o arquivo para leitura ('r' de read)
with open('capitais_brasil.csv', 'r', encoding='utf-8') as arquivo:
    # Ler todas as linhas de uma vez e guardar numa lista
    linhas = arquivo.readlines()

# Mostrar as primeiras linhas pra ver se leu certo (pra teste)
print(linhas[:3])  # Mostra as 3 primeiras linhas

print(len(linhas))