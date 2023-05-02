from Questao03 import calculaMedia

def test_calculaMedia():
  notas = [0, 10 , 10, 8, 6]
  assert calculaMedia(notas) == 6.8
  
  notas = [10, 5, 8, 10, 6]
  assert calculaMedia(notas) == 7.8

  notas = [10, 8]
  assert calculaMedia(notas) == 9.0
#
