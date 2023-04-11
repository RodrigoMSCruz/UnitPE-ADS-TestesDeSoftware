#Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
#
#    FULANO
#    FULAN
#    FULA
#    FUL
#    FU
#    F

def nomeNaVertical(nome):
    for l in range(len(nome) - 1, -1, -1):
        for c in range(0, l+1):
            print(nome[c], end='')
        #
        print()    
    #
#

nomeEntrada = input('Digite um nome: ')
nomeNaVertical(nomeEntrada)