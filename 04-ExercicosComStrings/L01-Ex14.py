# Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. 
# A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo
# muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que
# peça uma texto e transforme-o para a grafia leet speak. 

def leetSpeakGenerator(text):
    leetSpeaktext = ''
    for c in text:
        if c == 'a' or c == 'A':
            leetSpeaktext += '@'
        #
        elif c == 'e' or c == 'E':
            leetSpeaktext += '3'
        #
        elif c == 'g' or c == 'G':
            leetSpeaktext += '9'
        #
        elif c == 'h' or c == 'H':
            leetSpeaktext += '|-|'
        #
        elif c == 'i' or c == 'I':
            leetSpeaktext += '1'
        #
        elif c == 'o' or c == 'O':
            leetSpeaktext += '0'
        #
        elif c == 's' or c == 'S':
            leetSpeaktext += '5'
        #
        else:
            leetSpeaktext += c
        #
    #
    return leetSpeaktext
#

textoEntrada = input('Digite um texto para gerar um Leak Speak: ')
print(leetSpeakGenerator(textoEntrada))