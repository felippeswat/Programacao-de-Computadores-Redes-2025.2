from msilib.schema import Media


print('Vamos calcular a média de um aluno do IFRN no segundo semestre de 2025')

nota1       =int(input('Informe a nota da ETAPA1: '))
nota2       =int(input('Informe a nota da ETAPA2: '))

carhora     =int(input('Inofrme a carga horária da disciplina em h/a: '))
faltas      =int(input('Informe a quantidade de faltas do aluno: '))


media       =round((nota1*2 + nota2*3)/5)
frequencia  =round((1-(faltas/carhora))*100)

print(f'Nota da etapa 1: {nota1}')
print(f'Nota da etapa 2: {nota2}')
print(f'Média: {media}')

print(f'Total de aulas: {carhora}')
print(f'Total de faltas: {faltas}')
print(f'Frequencia do aluno: {frequencia}%')

if (media>=60):
    print('APROVADO')
elif (media>=20):
    print('PROVA FINAL')
else:
    print('REPROVADO')