from app.Employee import Employee
from dataclasses import is_dataclass
import pytest
from pytest import mark


@pytest.fixture
def funcionario():
    return Employee(10, 'João José', 'joaojose@souunit.com.br', 3500.00)


def test_constructor(funcionario: Employee):
    
    #funcionario = Employee(10, 'João José', 'joaojose@souunit.com.br', 3500.00)
    assert funcionario.id == 10
    assert funcionario.nome == 'João José'
    assert funcionario.email == 'joaojose@souunit.com.br'
    assert funcionario.salario == 3500.00


def test_ifIsADataclass(funcionario: Employee):
    
    #funcionario = Employee(10, 'João José', 'joaojose@souunit.com.br', 3500.00)
    assert is_dataclass(funcionario) == True


@mark.Salario
def test_increaseSalaryPercent(funcionario: Employee):
    
    #funcionario = Employee(10, 'João José', 'joaojose@souunit.com.br', 3500.00)
    funcionario.aumenta_salario(10)
    assert funcionario.salario == 3850


@mark.Salario 
def test_decreaseSalaryPercent(funcionario: Employee):

    #funcionario = Employee(10, 'João José', 'joaojose@souunit.com.br', 3500.00)
    funcionario.diminui_salario(25)
    assert funcionario.salario == 2625

