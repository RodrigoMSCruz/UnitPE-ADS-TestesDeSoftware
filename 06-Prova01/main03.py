
notas = []

def calculaMedia(vetorNotas):
  somatorio = 0
  quantidade = 0
  
  for n in vetorNotas:
    somatorio += n
    quantidade += 1
  #
  return somatorio/quantidade
#

#while True:
#  notaLida = float (input ('Digite uma nota (-1 para parar): '))
#  if notaLida == -1:
#    break
#  #
#  else:
#    notas.append(notaLida)
#  #


#print('A média é: ', calculaMedia(notas))

