def pi(loop):
    d = 0
    for l in range(loop):
        d += ((-1) ** l ) * ((2 * l + 1)**(-1))
    return d *4


print(pi(100000))