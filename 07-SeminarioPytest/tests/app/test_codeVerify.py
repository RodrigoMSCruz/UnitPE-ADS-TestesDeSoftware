from app.VerificaCodigo import checa_codigo, soma2numeros
from pytest import mark
import sys

def test_vazio():
  assert checa_codigo('') == False


def test_comprimento():
  assert checa_codigo('88888888') == True
  assert checa_codigo('0123') == False
  assert checa_codigo('01347984') == True


def test_letras():
  assert checa_codigo('123456a9') == False
  assert checa_codigo('b9876543') == False
  assert checa_codigo('cOd1g0') == False


def test_caracteresEspeciais():
  assert checa_codigo('@1234567') == False
  assert checa_codigo('@!#$%&*+') == False
  assert checa_codigo('81-987_4') == False


def test_espacosNoComecoOuNoFinal():
  assert checa_codigo(' 85431294 ') == True
  assert checa_codigo(' 98765432') == True
  assert checa_codigo('87457981 ') == True


def test_muitasPossibilidades():
  assert checa_codigo(' 12$56') == False
  assert checa_codigo('78%3 A') == False
  assert checa_codigo('r1%@') == False
  assert checa_codigo(' Err@d0 ') == False
  assert checa_codigo('T35t3 3rr4d0! 56') == False


'''
@mark.parametrize(
  'param, waited_result',
  [
    ('77777777', True),
    ('0123', False),
    ('98765432', True)
  ]   
)
def test_lenght_with_parametrize(param,waited_result):
  assert checa_codigo(param) == waited_result
'''