def soma(*params):
    print(params)

soma(11,2,3,4)


#faça uma função que some todos os argumentos que ela receber
def somas  (*d):
    res = 0
    for i in d:
        res += i
    return res
print(somas(2,2,2,2,2,2,2))