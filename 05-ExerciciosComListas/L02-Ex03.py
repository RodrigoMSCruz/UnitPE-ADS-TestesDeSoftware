# Faça um Programa que leia 4 notas, mostre as notas e a média na tela. 

def media4Notas(notas):
    somatorio = 0
    for n in notas:
        somatorio += n
    #
    return somatorio / len(notas)
#


notasEntrada = []

for i in range(0, 4):
    nota = int(input('Digite uma nota: '))
    notasEntrada.append(nota)
#

print('A média é: ', media4Notas(notasEntrada))