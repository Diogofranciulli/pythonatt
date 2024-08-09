n = int(input("digite um numero"))

est = "*"

for i in range(1, n + 1):
    print(f"{est:^{n*2-1}}")
    antigas = est
    est = est + "**"
