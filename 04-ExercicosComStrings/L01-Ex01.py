#Tamanho de strings. 
#Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais
# ou diferentes no conteúdo.

#    Compara duas strings
#    String 1: Brasil Hexa 2006
#    String 2: Brasil! Hexa 2006!
#    Tamanho de "Brasil Hexa 2006": 16 caracteres
#    Tamanho de "Brasil! Hexa 2006!": 18 caracteres
#    As duas strings são de tamanhos diferentes.
#    As duas strings possuem conteúdo diferente.

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
str2 = input('Digite o texto 2: ')
comparaStrings(str1, str2)