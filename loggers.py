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
    print("Введите имя файла: ")
    file_name = input()
    data = open(file_name + '.txt', 'r', encoding='utf-8')  
    print(data.read())
    data.close()

    data = open(file_name + '.txt', 'w', encoding='utf-8')
    print("Введите новые ФИО и номер телефона (+7) через пробел: ")
    original_data = input()
    data.write(original_data)
    data.close()


