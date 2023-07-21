#from random import randint as rd
n = int(input("Введите количество элементов списка: "))
data_list = list()
for i in range(n):
    data_list.append(int(input("Введите элемент: ")))
set1 = set(data_list)   
print(f"В данном списке {len(set1)} различных чисел")