
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