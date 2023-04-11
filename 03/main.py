def par_impar(num):
    if num % 2 == 0:
        return True
    else:
        return False

def teste_numero():
  #Assert
  assert par_impar(10) == True
  assert par_impar(11) == False

def inverter(palavra):
  nova_palavra = ""
  for c in palavra:
    if c == "a" or c == "e" or c == "i" or c == "o" or c =="u" or c == "A" or c == "E" or c == "I" or c == "O" or c =="U":
      nova_palavra += "#"
    else:
      nova_palavra += c
  return nova_palavra