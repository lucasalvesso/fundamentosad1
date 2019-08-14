def converte(numBinario, base):
    cont = 0
    numBinario = str(numBinario)
    numConvertido = []
    for i in range(len(numBinario)):
        if cont == 0:
            cont = (0 * base) + int(numBinario[i])
        else:
            cont = (cont * base) + int(numBinario[i])
    
    for i in range(3, 11):
        minimal = cont
        total = []
        while minimal > 0:
            total.append(str(minimal % i))
            minimal = minimal / i 
            minimal = int(minimal)
        numConvertido.append("".join(total[::-1]))
    
    numConvertido = " ".join(numConvertido)
    return numConvertido

var = 0
while var == 0:
    entrada = int(input("Digite o número a ser convertido: "))
    if entrada < 0:
        var = 1
    else:
        print(converte(entrada, 2))
    