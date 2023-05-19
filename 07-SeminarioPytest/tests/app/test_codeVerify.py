from app.CodeVerify import check_code
from pytest import mark

def test_empty():
  assert check_code('') == False


def test_lenght():
  assert check_code('88888888') == True
  assert check_code('0123') == False
  assert check_code('01347984') == True


@mark.parametrize(
'param, waited_result',
[('77777777', True),('0123', False),('98765432', True)]   
)
def test_lenght_with_parametrize(param,waited_result):
  assert check_code(param) == waited_result


def test_letters():
  assert check_code('123456a9') == False
  assert check_code('b9876543') == False
  assert check_code('cOd1g0') == False
  

def test_specialChars():
  assert check_code('@1234567') == False
  assert check_code('@!#$%&*+') == False
  assert check_code('81-987_4') == False


def test_blankSpacesInBeginingOrInTheEnding():
  assert check_code(' 85431294 ') == True
  assert check_code(' 98765432') == True
  assert check_code('87457981 ') == True


def test_manyPossibilites():
  assert check_code(' 12$56') == False
  assert check_code('78%3 A') == False
  assert check_code('r1%@') == False
  assert check_code(' Err@d0 ') == False
  assert check_code('T35t3 3rr4d0! 56') == False
  
  #Organização de Pastas - Boas Normas
  # Arquivo __init__.py em tests.
  
  #pytest -v --> Detalhamento