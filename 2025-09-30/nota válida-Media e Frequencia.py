from msilib.schema import Media
import sys

print('Vamos calcular a média de um aluno do IFRN no segundo semestre de 2025')

nota1       =int(input('Informe a nota da ETAPA1: '))
if not(nota1>=0 and nota1<=100):
    sys.exit('Nota 1 inválida')


nota2       =int(input('Informe a nota da ETAPA2: '))
if not(nota2>=0 and nota2 <=100):
    sys.exit('Nota 2 Inválida')

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

if (media>=60) and (frequencia>=75):
    print('APROVADO')
elif (media>=20) and (frequencia>=75):
    print('PROVA FINAL')
else:
    print('REPROVADO')