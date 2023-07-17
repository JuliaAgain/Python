n = int(input("Введите 1-е число: "))
m = int(input("Введите 2-е число: "))
if n > m:
    print(f'Число {n} больше чем {m}.')
elif n < m:
    print(f'Число {m} больше чем {n}.')
else:
    print('Числа равны')    
