# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números. 

def calculaVetor(vetor):
    soma = 0
    multiplicacao = 1
    for n in vetor:
        soma += n
        multiplicacao *= n
    #
    print('Números: ', vetor)
    print('Soma: ', soma)
    print('Multiplicação: ', multiplicacao)
#

numeros = []
for i in range(0,5):
    numeros.append( int (input('Digite um número:' )))
#
calculaVetor(numeros)