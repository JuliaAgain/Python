n = int(input("Введите число дней: "))
max_warmth = 0 # самая долгая оттепель (число дней)
warm = 0 # текущая оттепель (число дней)
for i in range(n):
    x = int(input("Введите температуру: "))
    if x > 0:
        warm+=1
        if warm > max_warmth:
            max_warmth = warm
    else:
        warm = 0
print(max_warmth)        

