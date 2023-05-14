#   Program001. Содержит функции с основными алгоритмами по обработке данных файла

#  import interface
from os import system
from Program002 import *


def add_contact(contact):
    #    contact = [input('Введите имя: ')+" ", input('Введите фамилию: ')+" ", input('Введите отчество: ')+" ", input('Введите телефон: ')]
    #  Определим кол-во строк в файле для назначения ID вновь вводимой строке (ID = count + 1)
    #
    # open file in read mode
    if len(contact) < 2:
        pass
    else:
        with open('file.txt', 'r', encoding='utf-8') as fp:
            for count, line in enumerate(fp):
                pass
            id_next = count + 1 + 1
#
        with open('file.txt', 'a', encoding='utf-8') as data:
            data.write(contact + ";" + str(id_next) + "\n")
# data.write('\n')
        data.close()


def seek_contact(name):
    #  функция выполняется только в том случае, если длина поисковой строуи содержит более одного символа
    if len(name) > 1:
        with open('file.txt', 'r', encoding='utf-8') as contact_list:
            k = 0
            for x in contact_list:
                y = x.split(";")
                if name.lower() in y[0].lower():
                    k += 1
                    print(y[0], y[4],  "->", x)
        contact_list.close()
        if k == 0:
            print("Ничего не найдено...")
        else:
            pass
        input("для продолжения нажмите клавишу Enter...")
    else:
        input("Поисковая строка не определена. Для продолжения нажмите клавишу Enter...")
#
#


def print_list():
    with open('file.txt', 'r', encoding='utf-8') as contact_list:
        i = 1
        for x in contact_list:
            print(f'{i}. {x}')
            i += 1
    contact_list.close()
    # system("cat -n file.txt")
    input("для продолжения нажмите клавишу Enter....")


def delete_contact(name):
    #  функция выполняется только в том случае, если длина поисковой строуи содержит более одного символа
    if len(name) > 1:
        with open('file.txt', 'r', encoding='utf-8') as contact_list:
            k = 0
            id_list = []
            for x in contact_list:
                y = x.split(";")
                if name.lower() in y[0].lower():
                    k += 1
                    print(y[0], y[4],  "->", x)
                    # массив порядковых номеров записей в файле, отобранных для удаления
                    id_list.append(int(y[4]))
        contact_list.close()
        #
        # далее обработка удаления найденных записей
        #
        if k == 0:
            input("Ничего не найдено...Для продолжения нажмите клавишу Enter....")
        elif k == 1:   # вызов функции удаления
            inp = input(
                "Для подтверждения удаления нажмите клавишу Y + Enter....")
            if inp == "Y" or inp == "y" or inp == "Н" or inp == "н":
                delete_line("file.txt", id_list[0], True)
                input("Запись удалена. Для продолжения нажмите клавишу Enter....")
            else:
                pass
        else:
            try:
                id_delete = int(
                    input("Укажите номер записи, которую нужно удалить " + "".join(str(id_list) + ": ")))
            except ValueError:  # Обработка если введена не цифра
                id_delete = 0
                print("Error! Это не число, повторите ввод через основное меню.")
            except EOFError:
                id_delete = 0
                print("EOFError! Выходим в основное меню...")
            else:
                if id_delete in id_list:

                    inp = input(
                        "Для подтверждения удаления нажмите клавишу Y + Enter....")

#                else:
                    if inp == "Y" or inp == "y" or inp == "Н" or inp == "н":
                        delete_line("file.txt", id_delete, True)
                        input(
                            "Запись удалена. Для продолжения нажмите клавишу Enter....")
                    else:
                        pass
                else:
                    input(
                        "Ощибка в номере записи. Для продолжения нажмите клавишу Enter....")

    # contact_list = open('file.txt', 'r', encoding='utf-8')
    # cash_list = []
    # for i in contact_list:
    #     if search in i:
    #         continue
    #     cash_list.append(i)
    # contact_list.close()

    # contact_list = open('file.txt', 'w', encoding='utf-8')
    # for i in cash_list:
    #     contact_list.writelines(i)
    # contact_list.close()


def update_contact(name):

 #  функция выполняется только в том случае, если длина поисковой строуи содержит более одного символа
    if len(name) > 1:
        with open('file.txt', 'r', encoding='utf-8') as contact_list:
            k = 0
            id_list = []
            for x in contact_list:
                y = x.split(";")
                if name.lower() in y[0].lower():
                    k += 1
                    print(y[0], y[4],  "->", x)
                    # массив порядковых номеров записей в файле, отобранных для внесения изменений
                    id_list.append(int(y[4]))
        contact_list.close()
        #
        # далее обработка внесения изменений в запись
        #
        if k == 0:
            input("Ничего не найдено...Для продолжения нажмите клавишу Enter....")
        elif k == 1:   # вызов функции внесеия изменений
            newline = inp_newdata_contact(name, id_list[0])
            print("newline->", newline)
            inp = input(
                "Для подтверждения внесения изменения нажмите клавишу Y + Enter....")
            if inp == "Y" or inp == "y" or inp == "Н" or inp == "н":
                update_line("file.txt", id_list[0], newline, ";")
                input("Запись обработана. Для продолжения нажмите клавишу Enter....")
            else:
                pass
        else:
            try:
                id_delete = int(
                    input("Укажите номер записи, в которую нужно внести изменения " + "".join(str(id_list) + ": ")))
            except ValueError:  # Обработка если введена не цифра
                id_delete = 0
                print("Error! Это не число, повторите ввод через основное меню.")
            except EOFError:
                id_delete = 0
                print("EOFError! Выходим в основное меню...")
            else:
                if id_delete in id_list:
                    newline = inp_newdata_contact(name, id_delete)
                    print("newline->", newline)
                    inp = input(
                        "Для подтверждения внесения изменений нажмите клавишу Y + Enter....")
                    if inp == "Y" or inp == "y" or inp == "Н" or inp == "н":
                        update_line("file.txt", id_delete, newline, ";")
                        input(
                            "Запись обработана. Для продолжения нажмите клавишу Enter....")
                    else:
                        pass
                else:
                    input(
                        "Ощибка в номере записи. Для продолжения нажмите клавишу Enter....")

    # contact_list = open('file.txt', 'r', encoding='utf-8')
    # cash_list = []
    # for i in contact_list:
    #     if search in i:
    #         cash_list.append(interface.get_contact())
    #         continue
    #     cash_list.append(i)
    # contact_list.close()

    # contact_list = open('file.txt', 'w', encoding='utf-8')
    # for i in cash_list:
    #     contact_list.writelines(i)
    # contact_list.close()


def delete_line(filename, line_number, Flagid):
    #  Функция удаления записи из тектового файла
    #  Передаваемые параметры:
    #   - filename - имя файла, из которого удаляется строка
    #   - line_number - номер удаляемой записи, отсчет от начала файла, строки пронумерованы от 1
    #   - Flagid - флаг, включающий специфическую для определенного формата обработку записей в файле
    #   Специфика формата - в качестве разделителя между значениями используется ";",
    #   Запись заканчивается символом "\n". При значении параметра Flag = True в каждую запись после последнего  значения
    #   через разделитель заносится порядковый номер записи в файле, вслед за ним - символ "\n".
    #   Если Flag = False то перезапись файла после удаления строки (записи) выполняется без дополнительной обработки.
    #
    with open(filename, "r", encoding='utf-8') as file:
        lines = file.readlines()
        print(lines)
        if line_number <= len(lines):
            #            for i in lines:
            del lines[line_number - 1]
        else:
            print("Line", line_number, "not in file.")
            print("File has", len(lines), "lines.")

    with open(filename, "w", encoding='utf-8') as file:
        k = 0
        for line in lines:
            k += 1
            if Flagid:
                file.write(leftsplit(line, ";") + ";" + str(k) + "\n")
            else:
                file.write(line)

# update_line("file.txt", id_list[0], newline, True)


def update_line(filename, line_number, newline, splitter):
    #  Функция удаления записи из тектового файла
    #  Передаваемые параметры:
    #   - filename - имя файла, из которого удаляется строка
    #   - line_number - номер удаляемой записи, отсчет от начала файла, строки пронумерованы от 1
    #   - newline - новая строка, которую нужно поместить на место старой строки номер line_number
    #   - splitter - символ-разделитель в записи файла
    #   Специфика формата - в качестве разделителя между значениями используется ";",
    #   Запись заканчивается символом "\n". При значении параметра Flag = True в каждую запись после последнего  значения
    #   через разделитель заносится порядковый номер записи в файле, вслед за ним - символ "\n".
    #   Если Flag = False то перезапись файла после удаления строки (записи) выполняется без дополнительной обработки.
    #
    with open(filename, "r", encoding='utf-8') as file:
        lines = file.readlines()
        print(lines)
        if line_number <= len(lines):
            #            for i in lines:
            oldfields = lines[line_number-1].split(splitter)
            newfields = newline.split(splitter)

            for i in range(1, len(newfields)):
                if len(newfields[i]) > 0:
                    oldfields[i] = newfields[i]
            print(*oldfields)
            # for xx in newfields:
            #     if len(xx) > 0:
            #         oldfields[kk] = xx
            #         kk += 1
            #     else:
            #         pass
#   Формирукм новую строку массива
            lines[line_number-1] = ";".join(oldfields) + "\n"
        else:
            print("Line", line_number, "not in file.")
            print("File has", len(lines), "lines.")

    with open(filename, "w", encoding='utf-8') as file:

        for line in lines:
            file.write(line)

            # if Flagid:
            #     file.write(leftsplit(line, ";") + ";" + str(k) + "\n")
            # else:
            #     file.write(line)


def leftsplit(line, sep):
    # функция убирает справа все символы до первого разделителя sep справа и сам этот разделитель
    #  Возвращает полученную строку оставшихся символов
    # Пример:
    #  иванов;иван;иванович;1234567;\n  ->  иванов;иван;иванович;1234567
    #  На вход подаются:
    # - строка символов line
    # - символ-разделитель sep

    list_1 = list(line)
#    print(list_1)
    k = len(line)
#   print(k)
#   print(list_1[1])
    line2 = ""
    list_2 = []
    for i in range(k):
        list_2.append(list_1[k-i-1])
#    print(list_2)
    line2 = "".join(list_2[2:])
    list_2 = list(line2)
    k = k - 2
    list_1 = []
    for i in range(k-2):
        list_1.append(list_2[k-i-1])
#   print(*list_1)
    line2 = "".join(list_1)
    return line2


print(leftsplit("иванов;иван;иванович;123456789;1", ";"))
