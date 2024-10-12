a = [12,68,41,95,10,21]

aux = a[-1]
j = 4
print(a)
while j >= 0 and a[j] > aux:
    a[j+1] = a[j]
    j = j - 1
    print(a)
a[j+1] = aux
print(a)