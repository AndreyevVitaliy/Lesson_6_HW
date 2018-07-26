# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
path_migrations = os.path.join(current_dir, migrations)

if __name__ == '__main__':

    def look_for(path_dir, list_file, user_string):
        new_file_list = list()
        if not list_file:

            for root, dirs, files in os.walk(path_dir):

                for file_name in files:

                    if file_name.endswith(".sql"):
                        path_file = os.path.join(path_dir, file_name)

                        with open(path_file, "r") as file:
                            file_read = file.read()

                            if user_string in file_read:
                                new_file_list.append(path_file)
                                print(path_file)
        else:
            for file_name in list_file:

                with open(file_name, "r") as file:
                    file_read = file.read()

                    if user_string in file_read:
                        new_file_list.append(file_name)
                        print(file_name)

        print(new_file_list.__len__())
        return new_file_list


    list_file = list()
    while True:
        user_string = input("Введите строку поиска: ")
        if user_string.lower() == 'q':
            break

        list_file = look_for(path_migrations, list_file, user_string)




