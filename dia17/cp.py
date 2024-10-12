#ex 1
def compras(lista_de_compras,supermercado):
    valor = 0
    tem = []
    ntem = []
    for i in lista_de_compras:
        if i in supermercado:
            valor += supermercado[i]
            tem.append(i)
        else:
            ntem.append(i)
    return valor, tem, ntem

#ex 2
a = [85,11,22,33,55]
i=0
def ordena(a):
    for iter in range(len(a)-1,0,-1):
        for i in range(len(iter)):
            if a[i][1] > a[i+1][1]:
                aux = a[i]
                a[i] = a[i+1]
                a[i+1] = aux
        return a

print(ordena(a))

#ex 3
lista = [1,2,3,50,100]
aux = 50
def busca(lista, aux):
    for i in range(len(lista)):
        if lista[i] == aux:
            return i
    return -1

print(busca(lista,50))

#ex 4

def atual_estoque(estoque_atual, novos_itens):
    for i in novos_itens.key():
        if i in estoque_atual:
            estoque_atual[i] += novos_itens[i]
        else:
            estoque_atual[i] = novos_itens[i]
    return estoque_atual

#ex 5

def medalhas(olimpiadas, pais):
    for i in olimpiadas["data"]:
        if i ["name"] == pais:
            return i["name"],i["total_medals"],i["gold_medals"],i["silver_medals"],i["bronzze_medals"]