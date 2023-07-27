def fib(n):
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


n = int(input("Введите номер числа Фибоначчи: "))
print(fib(n))