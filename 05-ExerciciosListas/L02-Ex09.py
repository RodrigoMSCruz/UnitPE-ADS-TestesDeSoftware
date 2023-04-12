# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor. 

def calculaVetor(A):
    somatorio = 0
    for n in A:
        somatorio += n**2
    #
    print('O somatório dos quadrados dos valores do vetor é: ', somatorio)
#

vetor = []
for i in range(0,10):
    vetor.append(int(input('Digite um valor: ')))
#

calculaVetor(vetor)