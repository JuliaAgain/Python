#Дан массив, состоящий из целых чисел. Напишите
#программу, которая в данном массиве определит
#количество элементов, у которых два соседних и, при
#этом, оба соседних элемента меньше данного. Сначала
#вводится число N — количество элементов в массиве
#Далее записаны N чисел — элементы массива. Массив
#состоит из целых чисел.
list_1 = [1, 2, 3, 4, 1, 2, 5]
count = 0
for i in range(len(list_1)):
    if list_1[i] > list_1[i - 1] and list_1[i] > list_1[i + 1 - len(list_1)]:
        count += 1
print(count)       