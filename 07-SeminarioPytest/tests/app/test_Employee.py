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
    assert funcionario.name == 'João José'
    assert funcionario.email == 'joaojose@souunit.com.br'
    assert funcionario.salary == 3500.00


def test_ifIsADataclass(funcionario: Employee):
    
    #funcionario = Employee(10, 'João José', 'joaojose@souunit.com.br', 3500.00)
    assert is_dataclass(funcionario) == True

#@mark.salario
def test_increaseSalaryPercent(funcionario: Employee):
    
    #funcionario = Employee(10, 'João José', 'joaojose@souunit.com.br', 3500.00)
    funcionario.increase_salary(10)
    assert funcionario.salary == 3850

#@mark.salario 
def test_decreaseSalaryPercent(funcionario: Employee):

    #funcionario = Employee(10, 'João José', 'joaojose@souunit.com.br', 3500.00)
    funcionario.decrease_salary(25)
    assert funcionario.salary == 2625

