from random import randint as rd
n = int(input("Введите число кустов: "))
weight = []
for i in range(n):
    weight.append(rd(1, 15))
print(weight)
max_summa = 0
for i in range(n):
    if max_summa < weight[i - 1] + weight[i] + weight[(i + 1) % n]:
        max_summa = weight[i - 1] + weight[i] + weight[(i + 1) % n]
print(max_summa)

