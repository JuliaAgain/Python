import os
def find_data():
    print("Введите имя файла: ")
    file_name = input()
    data = open(file_name + '.txt', 'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()    

def new_data():
    print("Введите название нового файла: ")
    new_file_name = input()
    data = open(new_file_name + '.txt', 'w', encoding='utf-8')
    print("Введите ФИО и номер телефона (+7) через пробел: ")
    original_data = input()
    data.write(original_data)
    data.close()

def correction_data():
    print("Введите имя файла, который хотите отредактировать: ")
    file_name = input()
    data = open(file_name + '.txt', 'r', encoding='utf-8')  
    data_list = data.read().split()
    print(data.read())
    data.close()
    print("Что выхотите изменить в файле?")
    print("0 - все данные\n"
          "1 - фамилию\n"
          "2 - имя\n"
          "3 - отчество\n"
          "4 - номер телефона\n")
    task = int(input("Введите номер команды: "))
    if task not in [0, 1, 2, 3, 4]:
        print("Ошибочный запрос!")
    elif task == 0:
        data = open(file_name + '.txt', 'w', encoding='utf-8')
        print("Введите новые ФИО и номер телефона (+7) через пробел: ")
        original_data = input()
        data.write(original_data)
        data.close()
    elif task == 1:
        print("Введите новую фамилию: ")
        data_list[0] = input()
        new_data = ' '.join(data_list)
        data = open(file_name + '.txt', 'w', encoding = 'utf-8')
        data.writelines(new_data)
        data.close()
    elif task == 2:
        print("Введите новое имя: ")
        data_list[1] = input()
        new_data = ' '.join(data_list)
        data = open(file_name + '.txt', 'w', encoding = 'utf-8')
        data.writelines(new_data)
        data.close()
    elif task == 3:
        print("Введите новое отчество: ")
        data_list[2] = input()
        new_data = ' '.join(data_list)
        data = open(file_name + '.txt', 'w', encoding = 'utf-8')
        data.writelines(new_data)
        data.close()
    elif task == 4:
        print("Введите новый номер телефона: ")
        data_list[3] = input()
        new_data = ' '.join(data_list)
        data = open(file_name + '.txt', 'w', encoding = 'utf-8')
        data.writelines(new_data)
        data.close()    


def delete_data():
    print("Введите имя файла, который хотите удалить: ")
    file_name = input()
    os.remove(file_name + '.txt', dir_fd=None)




