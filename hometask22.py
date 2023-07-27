# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n =  int(input("Введите число элементов в первом списке: "))
m =  int(input("Введите число элементов во стором списке: "))
list1 = []
list2 = []
for i in range(n):
    num = int(input("Введите число из первого списка: "))
    list1.append(num)
for i in range(m):
    num = int(input("Введите число из второго списка: "))
    list2.append(num)
common_numbers = set(list1).intersection(set(list2))
common_numbers = sorted(list(common_numbers))
print(*common_numbers)