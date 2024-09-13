dia = 6

if dia == 1:
    print("domingo")
elif dia == 2:
    print("segunda")
elif dia == 3:
    print("terca")
elif dia == 4:
    print("quarta")
elif dia == 5:
    print("quinta")
elif dia == 6:
    print("sexta")
elif dia == 7:
    print("sabado")
else:
    print("dia invalido")

match dia:
    case 1:
        print("domingo")
    case 2:
        print("segunda")
    case 3:
        print("terca")
    case 4:
        print("quarta")
    case 5:
        print("quinta")
    case 6:
        print("sexta")
    case 7:
        print("sabado")
    case _:
        print("dia invalido")