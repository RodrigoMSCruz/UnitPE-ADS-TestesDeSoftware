from app.Funcionario import Funcionario
from dataclasses import is_dataclass
import pytest
from pytest import mark


@pytest.fixture
def funcionario_novo():
    return Funcionario(10, 'João José', 'joaojose@souunit.com.br', 3500.00)


def test_constructor(funcionario_novo: Funcionario):
    
    #funcionario = Funcionario(10, 'João José', 'joaojose@souunit.com.br', 3500.00)
    assert funcionario_novo.id == 10
    assert funcionario_novo.nome == 'João José'
    assert funcionario_novo.email == 'joaojose@souunit.com.br'
    assert funcionario_novo.salario == 3500.00


def test_ifIsADataClass(funcionario_novo: Funcionario):
    
    #funcionario = Employee(10, 'João José', 'joaojose@souunit.com.br', 3500.00)
    assert is_dataclass(funcionario_novo) == True


def test_increaseSalaryPercent(funcionario_novo: Funcionario):
    
    #funcionario_novo = Funcionario(10, 'João José', 'joaojose@souunit.com.br', 3500.00)
    funcionario_novo.aumenta_salario(10)
    assert funcionario_novo.salario == 3850

 
def test_decreaseSalaryPercent(funcionario_novo: Funcionario):

    #funcionario_novo = Funcionario(10, 'João José', 'joaojose@souunit.com.br', 3500.00)
    funcionario_novo.diminui_salario(25)
    assert funcionario_novo.salario == 2625

