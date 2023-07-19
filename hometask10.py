n = int(input("Введите число монеток: "))
count1 = 0 # число гербов
count0 = 0 # число решек
for i in range(n):
    x = int(input("Введите значение (1 - герб, 0 - монтетка): "))
    if x == 0:
        count0+=1
    elif x == 1:
        count1 +=1
if (count1 > count0):
    result = count0
else:
    result = count1
print(f"Нужно перевернуть {result} монет(-ы).") 

