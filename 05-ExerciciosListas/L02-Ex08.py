# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida. 

def mostraVetoresInvertidos(idade, altura):
    print('Idades:', end =' ')
    for i in range(len(idade)-1, -1, -1):
        print(idade[i], end = '  ')
    #
    print()
    print('Alturas: ', end= ' ')
    for a in range(len(altura)-1, -1, -1):
        print(altura[a], end = ' ')
    #
    print()
#


idades = []
alturas = []
for p in range(0,5):
    print('Pessoa ', p+1)
    idades.append( int( input('Digite a idade:')))
    alturas.append( input('Digite a altura:'))
#
mostraVetoresInvertidos(idades, alturas)