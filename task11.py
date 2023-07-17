n = int(input("Введите число: "))
a0 = 0
a1 = 1
x = 1
i = 2
while x < n:
    x = a0 + a1
    a0 = a1
    a1 = x
    i +=1
    if x > n:
        i = 0
if i != 0:
    print(i)
else:
    print(-1)