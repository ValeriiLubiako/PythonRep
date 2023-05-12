#  main.py


import interface
import func


def main_prog():
    flag = True
    while flag:
        a = interface.hello()
        if a == '1':
            func.add_contact(interface.get_contact())
        elif a == '2':
            func.search_contact()
        elif a == '3':
            func.print_all()
        elif a == '4':
            func.change_contact(interface.get_change_contact())
        elif a == '5':
            func.del_contact(interface.get_del_contact())
        else:
            flag = False


main_prog()
