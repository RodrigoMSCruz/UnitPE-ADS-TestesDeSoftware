
def inverter(palavra):
  resposta = ''
  for c in palavra:
    if (c == 'A') or (c == 'E'):
      resposta += '#'
    #
    else:
      resposta += c
  #
  return resposta
#