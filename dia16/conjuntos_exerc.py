a = set([1,2,3,4,5,6,7,8])
b = set([7,8,9,10,11,12,13,14])

comum = a & b
somentePrimeira = a - b
somenteSegunda = b - a
naoRepetido = a ^ b
print(comum)
print(somentePrimeira)
print(somenteSegunda)
print(naoRepetido)