a = [12,68,41,95,10,21]

for i in range(len(a)):
    aux = a[i]
    j = i-1
    while j >= 0 and a[j] > aux:
        a[j+1] = a[j]
        j = j - 1
    a[j+1] = aux

print(a)