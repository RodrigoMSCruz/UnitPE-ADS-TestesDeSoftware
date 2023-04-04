lista = []
maior = menor = 0
quant = int(input("Digite a quantidade de números a ser digitada: "))

for i in range(0, quant):
    numero = int(input("Digite o número: "))
    lista.append(numero)
    if i == 0:
        maior = menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
        
print("O maior número é: ", maior)
print("O menor número é: ", menor)

