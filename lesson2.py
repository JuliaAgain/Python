# for (int i = 0; i <= 10; i++)
# int[] array = {1, 45, -10, 23, 2}
# foreach (int element in array)

# range(начальное_значение=необязательный(по умолчанию 0), конечное_значение=обязательный,
#       шаг_итерации=необязательный(по умолчанию 1))
print(*range(5))  # [0; 5) + 1
print(*range(3, 7))
print(*range(3, 7, 10))
print(*range(3, 14, 2))
print(*range(10, -2, -1))

for i in range(5):
    print(i, end=' ')