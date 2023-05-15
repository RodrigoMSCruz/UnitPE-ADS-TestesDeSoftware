
def lengh_verify(code):
  
  if len(code) == 8:
    return True
  else:
    return False

def numeric_verify(code):
  
  #result = True
  for c in code:
    if c in ('0123456789'):
      result = True
    else:
      result = False
      break

  return result



def check_code(code):
  codeStrip = code.strip()
  return lengh_verify(codeStrip) and numeric_verify(codeStrip)

