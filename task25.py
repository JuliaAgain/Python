text = input("Введите текст: ").split()
d = {}
for char in text:
    if char in d:
        print(f"{char}_{d[char]}", end =' ')
        d[char] +=1
    else:
        print(char, end = ' ')
        d[char] = 1
    
 