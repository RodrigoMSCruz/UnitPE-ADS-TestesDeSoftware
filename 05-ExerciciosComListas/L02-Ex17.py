# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos 
# cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe
# o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o
#exemplo abaixo:

#Atleta: Rodrigo Curvêllo
 
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m

#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9 m


def mediaSaltos(nome):
    saltos = []

    saltos.append(float (input('Primeiro Salto: ')))
    saltos.append(float (input('Segundo Salto: ')))
    saltos.append(float (input('Terceiro Salto: ')))
    saltos.append(float (input('Quarto Salto: ')))
    saltos.append(float (input('Quinto Salto: ')))

    print('Resultado final:')
    print('Atleta: ', nome)
    print('Saltos: ', saltos[0], ' - ', saltos[1], ' - ', saltos[2], ' - ', saltos[3], ' - ', saltos[4])

    somatorio = 0
    for s in saltos:
        somatorio += s
    #
    media = somatorio / 5
    print('Média dos saltos: ', media, 'm')
#

while True:
    atleta = input('Atleta: ')
    if atleta == '':
        break
    #
    else:
        mediaSaltos(atleta)
    #
#