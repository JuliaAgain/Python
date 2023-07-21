from random import randint as rd  # alias(псевдоним)


n = int(input("Введите кол-во элементов списка: "))
k = int(input("Введите значение сдвига: "))
k = k % n
data_list = list()
for i in range(n):
    data_list.append(rd(-10, 10))
print(data_list)
result_list = []
for i in range(k):
    result_list.append(data_list[n - k + i])
for i in range(n-k):
    result_list.append(data_list[i])

print(result_list)
    
    