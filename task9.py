n = int(input("Введите число: "))
f = 1
i = 1
while i <= n:
    f *= i
    i+=1
print(f'{n}! = {f}')    
