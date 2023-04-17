#   Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas
#   nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar
#   o que se pode aproveitar deles.
#
#   Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma
#   contendo: um número de identificação do mouse o tipo de defeito:
#   necessita da esfera; necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado
#   Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório: 

#Quantidade de mouses: 100

#Situação                        Quantidade              Percentual
#1- necessita da esfera                  40                     40%
#2- necessita de limpeza                 30                     30%
#3- necessita troca do cabo ou conector  15                     15%
#4- quebrado ou inutilizado              15                     15%

mouseSN = []
mouseStatus = []
contador = 0


def quantidade(i):
    qStatus = 0
    for s in range(0, contador):
        if mouseStatus[s] == i:
            qStatus += 1
        #
    #
    return qStatus
#


def percentual(i):
    return (quantidade(i) / contador) * 100
#


while True:
    sn = input('Digite o SN do mouse (0 para parar): ')
    if sn == '0':
        break
    #
    else:
        mouseSN.append(sn)
        mouseStatus.append(input('#1-Necessita da esfera - #2-Necessita de limpeza - #3-Necessita troca do cabo ou conector - #4-Quebrado ou inutilizado: '))
        contador += 1
    #
#

print('Quantidade de mouses: ', contador)
print()
print('Situação                        Quantidade              Percentual')
print('1- necessita da esfera   ', quantidade('1'), percentual('1'), '%')
print('2- necessita de limpeza  ', quantidade('2'), percentual('2'), '%')
print('3- necessita troca do cabo ou conector   ', quantidade('3'), percentual('3'), '%')
print('4- quebrado ou inutilizado   ', quantidade('4'), percentual('4'), '%')

