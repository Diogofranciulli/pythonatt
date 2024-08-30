a = []
b= 0
for i in range(5):
    a.append(int(input(f"digite um valor para a posição {b} ")))
    b+=1
print(f"vc digitou  os valores {a}")
for c, v in enumerate(a):
     k = print(f"na posicao {c} o valor é {v}")

a.sort()
print(a)

for l in a:
    print(l)

print(f"o maior valor digitado foi {a[-1]}")
print(f"o menor valor digitado foi {a[0]}")
