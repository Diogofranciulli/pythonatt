# QUESTAO 1
def funcao(x):
    if x < -2:
        return x**2 + 3*x -4
    elif x< 0:
        return 2*x +5
    elif x < 4:
        return x ** 0.5
    elif x < 6:
        return x**3 -3*x**2 - 10*x
    elif x < 8:
        return 3*x**2 - 4*x - 20
    else:
        return 10


print(funcao(10))


# QUESTAO 2
def lerMatriz(l, c):
    matriz = []
    for j in range(l):
        linha = []
        for i in range(c):
            linha.append(int(input(":")))
        matriz.append(linha)

    return matriz


print(lerMatriz(1,1))

# QUESTAO 3
def tam(matriz1):
    linhas = len(matriz1)
    colunas = len(matriz1[0])
    return [linhas,colunas]


print(tam([[1,2,3], [4,5,6]]))


# QUESTAO 4
def sub(a,b):
    if tam(a)[0] == tam(b)[0] and tam(a)[1] == tam(b)[1]:
        c1 = []
        for j in range(len(a[0])):
            linha = []
            for i in range(len(a[0])):
                linha.append(a[j][i] - b[j][i])
            c1.append(linha)
        return c1
    else:
        return "matriz invalida"


a=[
    [5,4],
    [1,2]
]

b = [
    [9,5],
    [1, 0]
]

print(sub(a,b))

# QUESTAO 5

d = [
    [1,2,3],
    [4,5,6]

]

e = []

def transposta(d):
    for j in range(len(d[0])):
        linha2 = []
        for i in range(len(d)):
            linha2.append(d[i][j])
        e.append(linha2)
print(e)

