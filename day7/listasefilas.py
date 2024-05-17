fila = []
while True:
    acao = input("digite A para adicionar a fila ou R para remover da fila: ")

    if acao == 'A':
        nome = input("digite o nome da pessoa")
        fila.append(nome)
    elif acao == "R":
        rem = fila.pop(0)
        print(f'{rem} foi atendido')
        print(f"O tamanho da fila agr é de {len(fila)} pessoas")
    else:
        print("comando invalido")

    print(fila)
    enc = input('deseja encerrar a fila? (S para encerrar e N para não encerrar)')
    if enc == 'S':
        break
print(fila)

