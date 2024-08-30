matriz = [
    [1,2,3],
    [5,6,7],
    [8,9,0]
]
def printa(matriz):
    for linha in matriz:
        for elemento in linha:
            print(elemento, end= " ")
        print()
printa(matriz)