from msilib.schema import Media


print('Vamos calcular a média de um aluno do IFRN no segundo semestre de 2025')

nota1       =int(input('Informe a nota da ETAPA1: '))
nota2       =int(input('Informe a nota da ETAPA2: '))

media       =round((nota1*2 + nota2*3)/5)

print(f'Nota da etapa 1: {nota1}')
print(f'Nota da etapa 2: {nota2}')
print(f'Média: {media}')
