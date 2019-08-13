from random import randint

def gerar(linha, coluna, matriz):
    for i in range(int(linha)):
        c = []
        for j in range(int(coluna)):
            c.append(randint(100, 999))
        matriz.append(c)
    return matriz

def posicao(matriz):
    pos = []
    maior = 0
    for i in matriz:
        for j in i:
            if j > maior:
                maior = j
                pos = [matriz.index(i), i.index(j)]
    return maior, pos

def somaLinha(matriz):
    total = []
    for i in matriz:
        soma = 0
        for j in i:
            soma += j
        total.append(soma)
    return total

def somaColuna(matriz):
    total = []
    var = 0
    while var < len(matriz[0]):
        col=0
        for i in matriz:
            col += i[var]
        total.append(col)
        var += 1
    return total

entrada = input("Digite as dimensões da matriz: ")
entrada = entrada.split()

matriz = []

print(gerar(entrada[0], entrada[1], matriz))
print(posicao(matriz))
print(somaLinha(matriz))
print(somaColuna(matriz))