#   Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
#   Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
#
#
#  main.py

from Program001 import *
from Program002 import *


def main_prog():
    flag = True
    while flag:
        # a = hello()
        # if a == '1':
        #     func.add_contact(interface.get_contact())
        # elif a == '2':
        #     func.search_contact()
        # elif a == '3':
        #     func.print_all()
        # elif a == '4':
        #     func.change_contact(interface.get_change_contact())
        # elif a == '5':
        #     func.del_contact(interface.get_del_contact())
        # else:
        #     flag = False

        match a:
            case "1":
                add_contact(interface.get_contact())

            case "2":
                search_contact()

            case "3":
                print_all()

            case "4":
                change_contact(interface.get_change_contact())

            case "5":
                del_contact(interface.get_del_contact())
            case _:
                flag = False


main_prog()
