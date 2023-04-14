#Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:

#"Qual o melhor Sistema Operacional para uso em servidores?"

#As possíveis respostas são:

#1- Windows Server
#2- Unix
#3- Linux
#4- Netware
#5- Mac OS
#6- Outro

def calculaPercentual(i, votos):
    somatorio = 0
    for v in votos:
        somatorio += v
    #
    return (votos[i]/somatorio) * 100
#


def melhorSO(votos):
    melhor = maisVotos = 0
    for i in range(0, 7):
        if i == 1:
            melhor = i
            maisVotos = votos[i]
        #
        else:
            if votos[i] > maisVotos:
                melhor = i
                maisVotos = votos[i]
            #
        #
    #
    resposta = 'O sistema operacional mais votado foi o ', so[melhor], 'com ', maisVotos, ' votos, correspondendo a ', calculaPercentual(melhor, votos), '%/ dos votos'
    return resposta
#


votos = [0,0,0,0,0,0,0]
so = ['', 'Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']

while True:
    escolha = int(input('Melhor Sistema Operacional (0=fim): '))
    
    if (escolha >= 1) and (escolha <= 6):
        votos[escolha] +=1
    #
    if (escolha <= -1) or (escolha >= 7):
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
    #
    if escolha == 0:
        break
    #
#

print('Resultado da votação:')
print('Sistema Operacional  Votos       %')
print('-------------------  -----       --')
for i in range(0, 7):
    if votos[i] != 0:
        print(so[i], '          ', votos[i], '  ', calculaPercentual(i, votos),'%')
    #
#
print(melhorSO(votos))