# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
# elementos intercalados dos dois outros vetores.

def intercalaVetores(v1, v2):
    vetorFinal = []
    for i in range(0, 10):
        vetorFinal.append(v1[i])
        vetorFinal.append(v2[i])
    #
    print('Vetor final: ', vetorFinal)
#

vetor1 = []
vetor2 = []
for i in range(0, 10):
    vetor1.append(int (input('Digite um valor para o vetor 1: ')))

print()

for i in range(0, 10):
    vetor2.append(int (input('Digite um valor para o vetor 2: ')))

intercalaVetores(vetor1, vetor2)