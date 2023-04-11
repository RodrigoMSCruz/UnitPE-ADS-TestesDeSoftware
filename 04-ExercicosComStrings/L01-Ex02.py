
def inverterECaixaAlta(texto):
    textoCaixaAlta = texto.upper()
    textoInvertido = textoCaixaAlta[::-1]
   
    return textoInvertido
#


palavra = input('Digite um texto:')
print(inverterECaixaAlta(palavra))