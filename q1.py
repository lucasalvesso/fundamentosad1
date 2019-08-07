def check(ipt, numeros, const):
    if len(ipt) == 0:
        display(numeros)
        const = 1
        exit()
    else:
        try:
            ipt = float(ipt)
            numeros.append(ipt)
        except:
            pass

def display(numeros):
    print("A quantidade de strings não vazias lidas: \n {}".format(len(numeros)))
    total = 0
    for n in numeros:
        total += n
    print("Média dos valores: \n {}".format((total)/(len(numeros))))
    print("O valor do maior número lido: \n {}".format(max(numeros)))

numeros = []
const = 0
while const == 0:
    check(input(), numeros, const)