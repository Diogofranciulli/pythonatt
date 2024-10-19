#for i in range(10):
#    nota = int(input("digite a nota: (0 ate 10)"))
#    if nota <= 10 and nota >= 0:
#        print(f"a nota digitada eh {nota}")
#        break
#    else:
#        print("Nota invalida")

#for i in range(10):
#    user = input("digite o nome de usuario")
#    password = input("digite a senha")
#
#    if user == password:
#        print("Usuario e senha nao podem ser iguais")
#    else:
#        print("Usuario e senha validos")
#        break


#for i in range(10):
#    while True:
#
#        nome = input("digite o nome:")
#        if len(nome) > 3:
#            break
#        else:
#            print("o nome precisa ser maior que 3 caracteres")
#
#    while True:
#        idade = int(input("digite a idade:"))
#        if idade > 0 and idade <= 150:
#            break
#        else:
#            print("precisa ser uma idade valida")
#
#    while True:
#        salario = float(input("digite o salario:"))
#        if salario >= 0:
#            break
#        else:
#            print("escreva um salario valido")
#
#    while True:
#        sexo = input("digite o sexo:").lower()
#        if sexo == "f" or sexo == "m":
#            break
#        else:
#            print("digite um sexo valido")
#
#    while True:
#        estado_civil = input("digite o estado civil: (s, c, v, d)")
#        if estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d":
#            break
#        else:
#            print("digite um estado civil valido")
#
#    break

#a = 80000
#
#b = 200000
#
#taxa_a = 3/100
#
#taxa_b = 1.5/100
#
#anos = 0
#
#while a < b:
#    a += a * taxa_a
#    b += b * taxa_b
#    anos += 1
#
#print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")
#
#
#a = int(input("digite o valor menor da populacao"))
#
#b = int(input("digite o valor maior da populacao"))
#
#taxa_a = int(input("digite o valor maior da taxa de crescimento")) / 100
#
#taxa_b = int(input("digite o valor menor da taxa de crescimento")) / 100
#
#anos = 0
#
#while a < b:
#    a += a * taxa_a
#    b += b * taxa_b
#    anos += 1
#
#print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")


#for i in range(0,20):
#    i += 1
#    print(i, end=" ")

#maior = None
#for i in range(5):
#    a = int(input("digite o numero"))
#
#    if maior is None or a > maior:
#        maior = a
#
#print(f"o maior numero eh {maior}")


