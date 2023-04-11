#Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
#
#    Data de Nascimento: 29/10/1973
#    Você nasceu em  29 de Outubro de 1973.

def DataPorExtenso(data):
    mes = ''
    if data[3:5] == '01':
        mes = ' de Janeiro'
    if data[3:5] == '02':
        mes = ' de Fevereiro'
    if data[3:5] == '03':
        mes = ' de Março'
    if data[3:5] == '04':
        mes = ' de Abril'
    if data[3:5] == '05':
        mes = ' de Maio'
    if data[3:5] == '06':
        mes = ' de Junho'
    if data[3:5] == '07':
        mes = ' de Julho'
    if data[3:5] == '08':
        mes = ' de Agosto'
    if data[3:5] == '09':
        mes = ' de Setembro'
    if data[3:5] == '10':
        mes = ' de Outubro'
    if data[3:5] == '11':
        mes = ' de Novembro'
    if data[3:5] == '12':
        mes = ' de Dezembro'
    #
    print('Você nasceu em ', data[0:2], mes, ' de ', data[6:10])
#

nascimento = input('Digite sua data de nascimento: (DD/MM/AAAA)')
DataPorExtenso(nascimento)