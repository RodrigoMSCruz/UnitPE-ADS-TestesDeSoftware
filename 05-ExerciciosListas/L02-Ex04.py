# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes. 

def contaConsoantes(vetor):
    qconsoantes = 0
    
    for c in vetor:
        if c not in ('aAeEiIoOuU'):
            print('Consoante: ', c)
            qconsoantes += 1
        #       
    #
    print('Número de consoantes: ', qconsoantes)
#

vetorEntrada = []
for i in range(0,10):
    caractere = input('Digite um caractér: ')
    vetorEntrada.append(caractere)                 
#

contaConsoantes(vetorEntrada)