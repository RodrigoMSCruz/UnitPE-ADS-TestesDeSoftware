
# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. 
# Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo
# de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não. 

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