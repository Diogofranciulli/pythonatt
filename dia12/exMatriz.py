valor = int(input("digite o valor para x"))
def funcao(valor):

    if valor >= 0 and valor < 5:
        print(f"O valor de y é {valor}")
    elif valor < 0:
        print(f"o valor de y é {valor ** 2}")
    elif valor > 5:
        print(f"o valor de y é {6}")
    else:
        print("erro")

funcao(valor)