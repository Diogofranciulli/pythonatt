a = [
    [0,0,0,1,4],
    [0,0,0,1,4],
    [0,0,0,1,4]
]


def esparsa(a):
    qtde = 0
    for i in a:
        for j in i:
            if j == 0:
                qtde += 1
                if qtde > len(a) * len(a[0]) / 2:
                    return True
    return False

print(esparsa(a))









