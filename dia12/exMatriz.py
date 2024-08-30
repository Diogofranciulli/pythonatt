valor = int(input("digite o valor para x"))
def funcao(valor):

    if valor >= 0:
        print(f"O valor de y é {valor}")
    elif valor < 0:
        print(f"o valor de y é {valor ** 2}")
    else:
        print("erro")

funcao(valor)