# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana
# recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam
# salários nos seguintes intervalos de valores:
#
#    $200 - $299
#    $300 - $399
#    $400 - $499
#    $500 - $599
#    $600 - $699
#    $700 - $799
#    $800 - $899
#    $900 - $999
#    $1000 em diante 

def categorizaSalarios(salarios):
    cat200_299 = cat300_399 = cat400_499 = cat500_599 = cat600_699 = cat700_799 = cat800_899 = cat900_999 = cat1000 = 0
    for s in salarios:
        if s>= 200 and s<= 299:
            cat200_299 += 1
        #
        if s>= 300 and s<= 399:
            cat300_399 += 1
        #
        if s>= 400 and s<= 499:
            cat400_499 += 1
        #
        if s>= 500 and s<= 599:
            cat500_599 += 1
        #
        if s>= 600 and s<= 699:
            cat600_699 += 1
        #
        if s>= 700 and s<= 799:
            cat700_799 += 1
        #
        if s>= 800 and s<= 899:
            cat800_899 += 1
        #
        if s>= 900 and s<= 999:
            cat900_999 += 1
        #
        if s>= 1000:
            cat1000 += 1
        #
    #
    print('$200 - $299: ', cat200_299)
    print('$300 - $399: ', cat300_399)
    print('$400 - $499: ', cat400_499)
    print('$500 - $599: ', cat500_599)
    print('$600 - $699: ', cat600_699)
    print('$700 - $799: ', cat700_799)
    print('$800 - $899: ', cat800_899)
    print('$900 - $999: ', cat900_999)
    print('$1000 em diante: ', cat1000) 

#

sal = [270, 470, 200, 820, 500, 1500, 420]
categorizaSalarios(sal)