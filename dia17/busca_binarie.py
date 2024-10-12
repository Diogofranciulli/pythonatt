lista = [12,25,37,38,41,53,59,68,71,95]
meio = len(lista) // 2

def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            fim = meio - 1
        else:
            inicio = meio + 1
    return None

print(busca_binaria(lista, 41))