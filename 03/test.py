from main import inverter


def test_size():
  assert inverter("") == ""


def test_aeiou():
  assert inverter("aeiou") == "#####"
  assert inverter("a e i o u") == "# # # # #"


def test_maiuscula_minuscula():
  assert inverter("Aa Bb Cc Dd Ee") == "## Bb Cc Dd ##"
  assert inverter("AAaa") == "####"


def test_caracter():
  assert inverter("-a-b") == "-#-b"
