from random import randint as rd
n = int(input("Введите число оценок: "))
marks = []
for i in range(n):
    marks.append(rd(1, 5))
print(marks)    
min_mark = min(marks)
max_mark = max(marks)
for i in range(n):
    if marks[i] == max_mark:
        marks[i] = min_mark
print(marks)        