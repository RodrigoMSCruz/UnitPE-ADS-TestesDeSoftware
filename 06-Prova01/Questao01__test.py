from Questao01 import existe_string

def test_existe_string():
  assert existe_string("joao", "joao e o pé de feijão") == True
  assert existe_string("maria", "joao e o pé de feijão") == False
  assert existe_string("eij", "joao e o pé de feijão") == True
  assert existe_string('Rodrigo', 'João e o pé de mandioca') == False
  assert existe_string('Testes','Q.A.') == False
  assert existe_string('Teste','Disciplina de Testes') == True
#
