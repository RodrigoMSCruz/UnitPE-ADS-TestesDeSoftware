from main import calcula_par


def test_par():
  assert calcula_par(20) is True
  assert calcula_par(3) is False
  assert calcula_par(0) is True
  assert calcula_par(-20) is True
  assert calcula_par(101) is False