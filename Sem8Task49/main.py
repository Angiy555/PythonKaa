#Задание 49
"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""
import os

os.system('CLS')

def show_all(file_name:str):
    """
    Функция принимает имя файла  (file_name) в иде строки
    и выводит телефонную книгу на экран
    """
    with open(file_name, 'r',encoding='utf-8') as fd:
        data = sorted(fd.readlines())
        print("".join(data))

def add_new(file_name: str):
    """
    Функция принимает имя файла  (file_name) в виде строки
    запрашивает у пользователя данные в виде ФИО и номер телефона
    и сохраняет полученные данные в файл
    """
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    #Открытие файла и запись в него данных в конце файла
    with open(file_name, 'a', encoding='utf-8') as fd:
        fd.write(f'{last_name}, {first_name}, {patronymic}, {phone_number}\n')
    os.system('CLS')

def find_by_atribute(file_name:str):
    """
    Функция принимает имя файла  (file_name) в виде строки
    запрашивает атрибут поиска и выводит результат поиска
    """
    temp = 0
    atribute = input("Введите данные для поиска: ")
    print()
    with open(file_name, 'r',encoding='utf-8') as fd:
        data = sorted([line.split(', ') for line in fd])
        for i in data:
            if atribute in i:
                print(*i)
                temp += 1
        if temp == 0:
            print('Такой записи нет в справочнике')

def modify(file_name:str):
    temp = 0
    find_data = []
    atribute = input("Введите данные для поиска: ")
    print()    
       
    with open(file_name, 'r',encoding='utf-8') as fd:
        data = sorted([line.split(', ') for line in fd])
        for i in data:
            if atribute in i:
                find_data.append(i)
                temp += 1
        if temp == 0:
            print('Такой записи нет в справочнике')

        for i in range(0, len(find_data)):
            print(f'{i + 1} {find_data[i]}')
        #print(list(zip(range(1,len(find_data)+1),find_data)))
        
        id = input("Введите id пользователя для изменения данных: ")
        
        #return data[int(id)-1]
    
    old_data = find_data[int(id)-1]
    print(old_data)
    
    print("Введите новые данные:\n")
    last_name_ = input('Введите фамилию: ')
    first_name_ = input('Введите имя: ')
    patronymic_ = input('Введите отчество: ')
    phone_number_ = input('Введите номер телефона: ')
    #data = ""
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        i = data.index(old_data)
        data[i] = f'{last_name_}, {first_name_}, {patronymic_}, {phone_number_}\n'
        
    with open(file_name, 'w',encoding='utf-8') as f:\
        f.writelines(data)

def remove(file_name:str):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    data = ""
    with open(file_name, 'r',encoding='utf-8') as fd:
        data = fd.readlines()
        s = f'{last_name}, {first_name}, {patronymic}, {phone_number}\n'
        data.remove(s)
    with open(file_name, 'w',encoding='utf-8') as fd:
        fd.writelines(data)



def main():
    """
    Основная функция
    """
    file_name = 'phonebook.txt'
    flag_exit = False
    while not flag_exit:
        print('1 - показать все записи телефонной книги')
        print('2 - добавить контакт в телефонную книгу')
        print('3 - поиск контакта в телефонной книге')
        print('4 - редактировать контакт в телефонной книге')
        print('5 - удалить запись из телефонной книги')
        answer = input('Введите операцию или х для выхода: ')
        if answer == '1':
            os.system('CLS')
            show_all(file_name)
        elif answer == '2':
            os.system('CLS')
            add_new(file_name)
        elif answer == '3':
            os.system('CLS')
            find_by_atribute(file_name)
        elif answer == '4':
            modify(file_name)
        elif answer == '5':
            remove(file_name)
        elif answer == 'x':
           flag_exit = True


if __name__ == '__main__':
    main()