n = int(input("Введите число арбузов: "))
x = int(input("введите массу арбуза: "))
minM, maxM = x, x
for i in range(n-1):
    x = int(input("введите массу арбуза: "))
    if x > maxM:
        maxM = x
    elif x < minM:
        minM = x
print(minM, maxM)
