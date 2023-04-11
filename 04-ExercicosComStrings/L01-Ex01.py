
def comparaStrings(texto1, texto2):
    print('Compara duas strings')
    print('String 1: ', texto1)
    print('String 2: ', texto2)
    print('Tamanho de ', texto1, ' : ', len(texto1), ' caracteres')
    print('Tamanho de ', texto2, ' : ', len(texto2), ' caracteres')
    if(len(texto1) == len(texto2)):
        print('As duas strings são de tamanhos iguais')
    #
    else:
        print('As duas strings são de tamanhos diferentes')
    #
    if (texto1 == texto2):
        print('As duas strings possuem conteúdo igual')
    #
    else:
        print('As duas strings possuem conteúdo diferente')
    #
#

str1 = input('Digite o texto 1: ')
str2 = input('Digite o texto 1: ')
comparaStrings(str1, str2)