#Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
#которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
#столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
#которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
#почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
#ровно два аргумента, как, например, у операции умножения.
#Ввод:** `print_operation_table(lambda x, y: x * y) ` 


def print_operation_table(operation, num_rows=6, num_columns=6):
    matrix = []
    for i in range(num_rows):    #заполняем матрицу заданных размеров нулями
        matrix.append([0]* num_columns)
    for i in range(num_rows):       #заполняем матрицу по условию
        for j in range(num_columns):
            matrix[i][j] = operation(i+1, j+1)
    for row in matrix:     #красиво выводим матрицу
        print(*row)



print_operation_table(lambda x, y: x * y)