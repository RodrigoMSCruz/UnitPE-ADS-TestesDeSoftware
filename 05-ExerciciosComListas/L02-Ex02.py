# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

def lerEMostraVetor():
    vetor = []
    for i in range(0, 10):
        valor = input('Digite um valor: ')
        vetor.append(valor)
    #
    for i in range(9, -1, -1):
        print(vetor[i], end=' ')
    #
#

lerEMostraVetor()