# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos. 

def contaAlunos(idades, alturas):
    cont = somatorio = 0

    for a in alturas:
        somatorio += a
    #

    media = somatorio / len(alturas)

    for i in range(0, 30):
        if (idades[i] > 13) and (alturas[i] < media):
            cont += 1
        #
    #

    return cont
#

vetorIdade = [13, 14, 14, 15, 16, 14, 13, 13, 12, 13, 14, 14, 15, 16, 14, 13, 13, 12, 13, 14, 14, 15, 16, 14, 13, 13, 12, 13, 14, 14]
vetorAltura = [1.50, 1.40, 1.35, 1.74, 1.80, 1.30, 1.60, 1.90, 1.54, 1.72, 1.73, 1.61, 1.63, 1.70, 1.56, 1.90, 1.73, 1.67, 1.64, 1.56, 1.70, 1.45, 1.89, 1.34, 1.45, 1.54, 1.63, 1.36, 1.50, 2.00]

print('A quantidade de alunos com alturas abaixo da média é: ', contaAlunos(vetorIdade, vetorAltura))