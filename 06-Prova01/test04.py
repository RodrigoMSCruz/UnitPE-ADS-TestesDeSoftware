from main04 import inverter 

def test_size():
    assert inverter("") == "" 


def test_aeiou(): 
    assert inverter("aeiou") == "aeiou" 
    assert inverter("a e i o u") == "a e i o u" 


def test_maiuscula_minuscula(): 
     assert inverter("Aa Bb Cc Dd Ee") == "#a Bb Cc Dd #e" 
     assert inverter("AAaa") == "##aa" 


def test_caracter(): 
     assert inverter("-a-b") == "-a-b"
