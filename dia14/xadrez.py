import matplotlib.pyplot as plt

xadrez = [
    [[255,255,255],[0,0,0],[255,255,255],[0,0,0],[255,255,255],[0,0,0],[255,255,255],[0,0,0]],
    [[0,0,0],[255,255,255],[0,0,0],[255,255,255],[0,0,0],[255,255,255],[0,0,0],[255,255,255]],
    [[255,255,255],[0,0,0],[255,255,255],[0,0,0],[255,255,255],[0,0,0],[255,255,255],[0,0,0]],
    [[0,0,0],[255,255,255],[0,0,0],[255,255,255],[0,0,0],[255,255,255],[0,0,0],[255,255,255]],
    [[255,255,255],[0,0,0],[255,255,255],[0,0,0],[255,255,255],[0,0,0],[255,255,255],[0,0,0]],
    [[0,0,0],[255,255,255],[0,0,0],[255,255,255],[0,0,0],[255,255,255],[0,0,0],[255,255,255]],
    [[255,255,255],[0,0,0],[255,255,255],[0,0,0],[255,255,255],[0,0,0],[255,255,255],[0,0,0]],
    [[0,0,0],[255,255,255],[0,0,0],[255,255,255],[0,0,0],[255,255,255],[0,0,0],[255,255,255]],

]

# plt.imshow(xadrez)
# plt.axis("off")
# plt.show()
linha = int(input(":"))
coluna = int(input(":"))
xadrez1 = [[[255*((i+j)%2),255*((i+j)%2),255*((i+j)%2)] for i in range (coluna)] for j in range(linha)]
print(xadrez1)

plt.imshow(xadrez1)
plt.axis("off")
plt.show()