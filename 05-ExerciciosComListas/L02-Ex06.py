# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0. 

def maioresMedias(medias):
    cont = 0
    for m in medias:
        if m >= 7:
            cont += 1
        #
    #
    print('O número de médias igual ou maior a 7 é ', cont) 
#



medias = []

for a in range(0,10):
    somatorio = 0
    for n in range(0,4):
        print('Aluno ', a+1)
        nota = int(input('Digite a nota: '))
        somatorio += nota
    #
    medias.append(somatorio/4)
#

maioresMedias(medias)