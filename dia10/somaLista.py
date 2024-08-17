#faça uma função que some todos os argumentos que ela receber
#peça pro usuario digitar a qtde de parametros que ele quer somar, os valores
#a serem somados, e realize a soma

quant = int(input("digite a qtde de valores que deseja somar"))

valores = []
for i in range(quant):
    valores.append(float(input("digite o valor")))

print(valores)

def somas  (*valores):
    res = 0
    for i in valores:
        res += i
    return res

print(somas(*valores))