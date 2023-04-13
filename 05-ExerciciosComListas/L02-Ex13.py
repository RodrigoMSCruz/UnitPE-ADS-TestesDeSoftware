# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas 
# acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ). 

def mesesAcimaDaMedia(temp):
    mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    somatorio = 0
    
    for t in temp:
        somatorio += t
    #

    media = somatorio / len(temp)
    print('A temperatura média do ano foi: ', media)
    print('Meses com temperatura acima da média: ', end= '')

    for m in range(0, 12):
        if temp[m] > media:
            print(mes[m], end = ' ')
        #
    #
#


temperaturas = [30, 26, 24, 25, 30, 31, 29, 28, 30, 32, 31, 24]
mesesAcimaDaMedia(temperaturas)