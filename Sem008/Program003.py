#   Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
#   Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
#
#
#  main.py

# содержит функции main.prog, с помощью которой реализуются основное меню,
# операций по обработке данных файла записной книжки.
# Файл должен быть расположен в текущем директории и называрься file.txt
# Программа запускается с этого файла.

from Program001 import *
from Program002 import *


def main_prog():
    flag = True
    while flag:
        a = salute()
        match a:
            case 1:
                print("Найти контакт/Find contact")
            case 2:
                print("Добавьте новый контакт/Add new contact")
            case 3:
                print("Список контактов/Contact list")
            case 4:
                print("Изменить/добавить данные о контакте/Update contact")
            case 5:
                print("Удалить контакт/Delete contact")
            case 6:
                print(
                    "ВНИМАИЕ! Будет удален ВЕСЬ СПИСОК КОНТАКТОВ/Attention! You will delete ALL YOUR CONTACTS!!!!")
                input(
                    "Данный режим пока не реализован.Нажмите Enter для продолжения работы...")
            case _:
                print("")
        print(a)
#       match a:
        if a == 1:
            seek_contact(inp_seek_contact())

        elif a == 2:
            add_contact(input_contact())

        elif a == 3:
            print_list()

        elif a == 4:
            update_contact(inp_update_contact())

        elif a == 5:
            delete_contact(inp_delete_contact())
        elif a == 6:
            pass
        else:
            flag = False


main_prog()
