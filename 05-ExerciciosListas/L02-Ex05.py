# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

def separaVetorParaEImpar(vetorTotal):
    vetorPar = []
    vetorImpar = []
    for i in vetorTotal:
        if i % 2 == 0:
            vetorPar.append(i)
        #
        else:
            vetorImpar.append(i)
        #
    #
    print('Vetor original:', end=' ')
    print(vetorTotal)
    print('Vetor Par:', end=' ')
    print(vetorPar)
    print('Vetor Ímpar:', end=' ')
    print(vetorImpar)
#

vetor = []
for i in range(0,20):
    vetor.append(int (input ('Digite um número inteiro: ')))
#
separaVetorParaEImpar(vetor)