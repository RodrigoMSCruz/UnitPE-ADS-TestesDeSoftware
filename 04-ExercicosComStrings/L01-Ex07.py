#Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
#
#    quantos espaços em branco existem na frase.
#    quantas vezes aparecem as vogais a, e, i, o, u. 

def contaEspacosEVogais(frase):
    espacos = vogais = 0
    for c in frase:
        if c == ' ':
            espacos += 1
        #
        if (c == 'a') or (c == 'A') or (c == 'e') or (c == 'E') or (c == 'i') or (c == 'I') or (c == 'o') or (c == 'O') or (c == 'u') or (c == 'U'):
            vogais += 1
        #     
    #
    print("A frase tem ", espacos, " espaços.")
    print("A frase tem ", vogais, " vogais.")
#

entrada = input('Digite uma frase: ')
contaEspacosEVogais(entrada)