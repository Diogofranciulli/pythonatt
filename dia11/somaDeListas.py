def listas():
    a = []
    b = []
    c = []

    for i in range(1,11):
        a.append(i)

    print(a)

    for l in range(1,11):
        b.append(l)

    print(b)

    for m in range(10):
        c.append(a[m] * b[m])
    return sum(c)





print(listas())