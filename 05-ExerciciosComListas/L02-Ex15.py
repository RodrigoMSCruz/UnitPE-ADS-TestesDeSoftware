# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1
# (que não deve ser armazenado). Após esta entrada de dados, faça:
#
#    Mostre a quantidade de valores que foram lidos;
#    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#    Calcule e mostre a soma dos valores;
#    Calcule e mostre a média dos valores;
#    Calcule e mostre a quantidade de valores acima da média calculada;
#    Calcule e mostre a quantidade de valores abaixo de sete;
#    Encerre o programa com uma mensagem; 

def calculaNotas():
    notas = []
    soma = acimadaMedia = abaixoDe7 = 0

    while True:
        n = int( input( 'Digite uma nota(-1 para sair): '))
        if n == -1:
            break
        #
        else:
            notas.append(n)
            soma += n
        #
    #

    print('Valores digitados: ', notas)
    print('Valores na ordem inversa que forma digitados e um em cima do outro:')
    
    for n in range(len(notas)-1, -1, -1):
        print(notas[n])
    #

    print('Somatório dos valores: ', soma)
    media = soma / len(notas)
    print('Média dos valores: ', media)

    for n in notas:
        if n > media:
            acimadaMedia += 1
        #
        if n < 7:
            abaixoDe7 += 1
        #
    #

    print('Quantitativo de notas acima da média: ', acimadaMedia)
    print('Quantitativo de notas abaixo de 7: ', abaixoDe7)
    print('Até mais!')
#


calculaNotas()