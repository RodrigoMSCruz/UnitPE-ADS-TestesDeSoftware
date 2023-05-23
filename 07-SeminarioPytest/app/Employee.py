from dataclasses import dataclass

@dataclass()
class Employee:
    
    id: int
    nome: str
    email: str
    salario: float

    def aumenta_salario(self, percent: float):
        self.salario = self.salario + (self.salario * (percent / 100))

    def diminui_salario(self, percent: float):
        self.salario = self.salario - (self.salario * (percent / 100))