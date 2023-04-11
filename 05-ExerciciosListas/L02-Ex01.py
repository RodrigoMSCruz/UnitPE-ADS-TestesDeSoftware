# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os. 

def lerEMostraVetor():
    vetor = []
    for i in range(0, 5):
        valor = input('Digite um valor: ')
        vetor.append(valor)
    #
    print(vetor)
#

lerEMostraVetor()