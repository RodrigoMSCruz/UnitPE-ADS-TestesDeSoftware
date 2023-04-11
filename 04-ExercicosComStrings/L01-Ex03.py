#Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
#
#    F
#    U
#    L
#    A
#    N
#    O

def nomeNaVertical(nome):
    for c in nome:
        print(c)
    #
#

nomeEntrada = input('Digite um nome: ')
nomeNaVertical(nomeEntrada)