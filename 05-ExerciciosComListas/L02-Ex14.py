# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#
#    "Telefonou para a vítima?"
#    "Esteve no local do crime?"
#    "Mora perto da vítima?"
#    "Devia para a vítima?"
#    "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
# deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 

def interrogatorio():
    respostas = []
    contsim = 0
    classificacao = "Inocente"

    respostas.append(input("Telefonou para a vítima? "))
    respostas.append(input("Esteve no local do crime? "))
    respostas.append(input("Mora perto da vítima? "))
    respostas.append(input("Devia para a vítima? "))
    respostas.append(input("Já trabalhou com a vítima? "))
    
    for r in respostas:
        if r == 'sim' or r == 'Sim' or r == 'SIM':
            contsim += 1
        #
    #
    if contsim == 2:
        classificacao = 'Suspeita'
    elif contsim == 3 or contsim == 4:
        classificacao = 'Cúmplice'
    elif contsim == 5:
        classificacao = 'Assasino'
    #
    print('Resultado do interrogatório: ', classificacao)
#

interrogatorio()
