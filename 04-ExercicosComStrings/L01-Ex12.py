# Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o 
#'3' na frente. O usuário pode informar o número com ou sem o traço separador.

#    Valida e corrige número de telefone
#    Telefone: 461-0133
#    Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
#    Telefone corrigido sem formatação: 34610133
#    Telefone corrigido com formatação: 3461-0133

def validaECorrigeNTelefone(numero):
    print('Valida e corrige número de telefone')
    print('Telefone: ', numero)
    numeroSemFormatacao = ''
    for n in numero:
        if n != '-':
            numeroSemFormatacao += n
        #
    #
    
    if len(numeroSemFormatacao) == 7:
        print('Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.')
        numeroSemFormatacao = '3' + numeroSemFormatacao
    #
    print('Telefone corrigido sem formatacao: ', numeroSemFormatacao)
    numeroFormatado = ''
    numeroFormatado = numeroSemFormatacao[0:4] + '-' + numeroSemFormatacao[4:9]
    print('Telefone corrigido com formatação: ', numeroFormatado)
#

numeroEntrada = input('Digite um número de telefone com formatação ou sem formatação: ')
validaECorrigeNTelefone(numeroEntrada)