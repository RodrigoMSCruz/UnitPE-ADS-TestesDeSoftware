
def palindromo(frase):
    frase = frase.upper()
    fraseSemEspaco = ''
    for c in frase:
        if c != (' '):
            fraseSemEspaco += c
        #
    #
    fraseSemEspacoInvertida = fraseSemEspaco[::-1]
    return fraseSemEspaco == fraseSemEspacoInvertida
#

entrada = input("Digite uma frase para testar se é um palíndormo: ")
print(palindromo(entrada))