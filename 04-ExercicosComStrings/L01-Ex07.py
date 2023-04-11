
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