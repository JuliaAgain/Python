from random import randint as rd
n = int(input("Введите кол-во элементов списка: "))
data_list = list()
for i in range(n):
    data_list.append(rd(-10, 10))
print(data_list)
count = 0
for i in range(n-1):
    if data_list[i+1] > data_list[i]:
        count+=1
print(count)