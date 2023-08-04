#Даны два массива чисел. Требуется вывести те элементы
#первого массива (в том порядке, в каком они идут в первом
#массиве), которых нет во втором массиве. Пользователь вводит
#число N - количество элементов в первом массиве, затем N
#чисел - элементы массива. Затем число M - количество
#элементов во втором массиве. Затем элементы второго массива
from random import randint
n = int(input("Введите число элементов в первом списке: "))
list1 = [randint(1, 10) for _ in range(n)]
m = int(input("Введите число элементов во втором списке: "))
list2 = [randint(1, 10) for _ in range(m)]
print(list1)
print(list2)
result = []
for i in list1:
    if i not in list2:
        result.append(i)
print(result)        
print([i for i in list1 if i not in list2])