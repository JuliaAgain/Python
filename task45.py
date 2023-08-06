def sum_dev(number: int):
    summa = 0
    for dev in range(1, number//2 + 1):
        if number%dev == 0:
            summa += dev
    return summa
k = int(input("Введите число k: "))
for m in range(1, k+1):
    n = sum_dev(m)
    if m == sum_dev(n) and m < n:
        print(m, n)

