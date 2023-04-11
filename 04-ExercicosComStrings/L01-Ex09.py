# Verificação de CPF.
# Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido
# através da validação dos dígitos verificadores edos caracteres de formatação.

def cpfValido(cpf):
    numbers = [int(digit) for digit in cpf if digit.isdigit()]
    
    sum_of_products  = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    
    if numbers[9] != expected_digit:
        return False
    #

    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    
    if numbers[10] != expected_digit:
        return False
    #
    return True
#

cpfEntrada = input("Digite o CPF no formato xxx.xxx.xxx-xx : ")
print(cpfValido(cpfEntrada))