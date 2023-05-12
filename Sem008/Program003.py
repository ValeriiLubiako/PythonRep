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
        a = salute()
        print(a)
#       match a:
        if a == 1:
                name = input('Фамилия:')
                seek_contact(name)
                
        elif a == 2:
            add_contact(input_contact())

        elif a == 3:
            print_all()

        elif a == 4:
            update_contact(interface.get_change_contact())

        elif a == 5:
            delete_contact(interface.get_del_contact())
        else:
            flag = False


main_prog()