
def verif_comprimento(code):
  if len(code) == 8:
    return True
  else:
    return False

def verif_numero(code):
  for c in code:
    if c in ('0123456789'):
      result = True
    else:
      result = False
      break
  return result

def checa_codigo(cod):
  codStrip = cod.strip()
  return verif_comprimento(codStrip) and verif_numero(codStrip)

