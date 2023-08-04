#Дан список чисел. Посчитайте, сколько в нем пар
#элементов, равных друг другу. Считается, что любые
#два элемента, равные друг другу образуют одну пару,
#которую необходимо посчитать. Вводится список
#чисел. Все числа списка находятся на разных
#строках
from random import randint
n = int(input("Введите число элементов в первом списке: "))
list1 = [randint(1, 5) for _ in range(n)]
print(list1)
pairs = 0
for item in set(list1):
    print(item, list1.count(item))
    pairs+= (list1.count(item) // 2)
print(pairs)     
print(sum([list1.count(item) // 2 for item in set(list1)]))