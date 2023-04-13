# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

def intercalaVetores(v1, v2, v3):
    vetorFinal = []
    for i in range(0, 10):
        vetorFinal.append(v1[i])
        vetorFinal.append(v2[i])
        vetorFinal.append(v3[i])
    #
    print('Vetor final: ', vetorFinal)
#

vetor1 = []
vetor2 = []
vetor3 = []

for i in range(0, 10):
    vetor1.append(int (input('Digite um valor para o vetor 1: ')))

print()

for i in range(0, 10):
    vetor2.append(int (input('Digite um valor para o vetor 2: ')))

print()

for i in range(0, 10):
    vetor3.append(int (input('Digite um valor para o vetor 3: ')))

intercalaVetores(vetor1, vetor2, vetor3)