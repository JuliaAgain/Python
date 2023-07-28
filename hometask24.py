from random import randint as rd
n = int(input("Введите число кустов: "))
weight = [] # список с массами ягод на каждом кусте
for i in range(n):
    weight.append(rd(1, 15))
print(*weight)
sum_of_3 = [] # cписок сумм кг для соседних 3 кустов
sum_of_3.append(weight[0] + weight[1]+ weight[-1])
sum_of_3.append(weight[0] + weight[-2]+ weight[-1])
for i in range(1, n-1):
    sum_of_3.append(weight[i-1] + weight[i]+ weight[i+1])

print(max(sum_of_3))

