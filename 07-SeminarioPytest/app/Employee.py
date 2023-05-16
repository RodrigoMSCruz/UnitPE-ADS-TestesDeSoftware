from dataclasses import dataclass

@dataclass()
class Employee:
    
    id: int
    name: str
    email: str
    salary: float

    def increase_salary(self, percent: float):
        self.salary = self.salary + (self.salary * (percent / 100))

    def decrease_salary(self, percent: float):
        self.salary = self.salary - (self.salary * (percent / 100))