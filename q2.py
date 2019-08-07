def add():
    entrada = input()
    if len(entrada) == 0:
        return "Nenhum número foi lido!!!"
    else:
        entrada = entrada.split()
        return cont(entrada)

def cont(entrada):
    c = [0, 0]
    for n in entrada:
        if entrada.count(n) > c[0]:
            c[0] = entrada.count(n)
            c[1] = n
    return "O número {} foi o que mais ocorreu: {} vez{}".format(c[1], c[0], "es." if c[0] > 1 else ".")

print(add())