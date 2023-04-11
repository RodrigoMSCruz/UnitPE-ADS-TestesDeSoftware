#Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
#
#    F
#    FU
#    FUL
#    FULA
#    FULAN
#    FULANO

def nomeNaVertical(nome):
    for l in range(0, len(nome)):
        for c in range(0, l+1):
            print(nome[c], end='')
        #
        print()    
    #
#

nomeEntrada = input('Digite um nome: ')
nomeNaVertical(nomeEntrada)