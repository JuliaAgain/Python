#Задача №49. Решение в группах
#Создать телефонный справочник с
#возможностью импорта и экспорта данных в
#формате .txt. Фамилия, имя, отчество, номер
#телефона - данные, которые должны находиться
#в файле.
#1. Программа должна выводить данные
#2. Программа должна сохранять данные в
#текстовом файле
#3. Пользователь может ввести одну из
#характеристик для поиска определенной
#записи(Например имя или фамилию
#человека)
#4. Использование функций. Ваша программа
#не должна быть линейной
tele01 = ['Иванов',  'Василий', 'Петрович', '+79267886554']
tele01 = ' '.join(tele01)
data = open('data01.txt', 'w', encoding = 'utf-8')
data.writelines(tele01)
data.close()

tele02 = ['Вачильченко', 'Евгений', 'Михайлович', '+79267676554']
tele02 = ' '.join(tele02)
data = open('data02.txt', 'w', encoding = 'utf-8')
data.writelines(tele02)
data.close()

tele03 = ['Петров', 'Евгений', 'Викторович', '+79267676554']
tele03 = ' '.join(tele03)
data = open('data03.txt', 'w', encoding = 'utf-8')
data.writelines(tele03)
data.close()

