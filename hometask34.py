#Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
#разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
#стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
#гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
#слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
#от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
#напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
#ввод: пара-ра-рам рам-пам-папам па-ра-па-дам 

def determine_if_rythm(string):
    phrases = string.split() # создаем список из фраз, разделенных пробелами
    number_of_vowels = []  # создаем список, где каждое число соответствует числу гласных в фразе
    for word in phrases:
        counter_vowels = 0   # счетчик гласных в каждой фразе
        for letter in word:  #перебираем каждую букву во фраз
            if letter in "аяоёэеыиую": #проверяем, является буква гласной
                counter_vowels +=1
        number_of_vowels.append(counter_vowels)     
    num = number_of_vowels[0] #проверяем, все ли числа в списке с чилами гласных равны
    rythm = True  
    for i in range(1, len(number_of_vowels)):
        if number_of_vowels[i] != num:
            rythm = False
    return rythm        


poem = input("Введите стих Винни-Пуха: ")
if determine_if_rythm(poem) == True:
    print("Парам пам-пам")
else:
    print("Пам парам")    