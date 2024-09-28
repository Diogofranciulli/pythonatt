a = [7,4,9,1,10,1]
print(a)


for j in range(len(a)-1,1,-1):
    for i in range(j):
        if a[i] > a[i+1]:
            aux = a[i]
            a[i] = a[i + 1]
            a[i + 1] = aux
print(a)