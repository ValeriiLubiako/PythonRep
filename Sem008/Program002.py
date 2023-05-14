# Program002.py
# Содержит функции, с помощью которых реализуются операции ввода-вывода

def salute():
    print("\n>>>>>>>------>>>>>>>>>>------>>>>>>>>>\n" +
          "Меню работы с записной книжкой.\n" +
          "Введите соответствующую выбранной операции цифру из списка:\n" +
          "- найти контакт/find contact: 1;\n" +
          "- добавить контакт/add contact: 2;\n" +
          "- просмотреть список контактов/list contacts: 3;\n" +
          "- внести изменения в контакт/upate contact: 4;\n" +
          "- удалить контакт/delete contact: 5;\n" +
          "- удалить ВЕСЬ список контактов/delete CONTACT LIST: 6;\n" +
          "- выйти из меню/escape: 7;\n")
    Flag = True
    while Flag:
        try:

            cn = input("-> ")
            n = int(cn)
            if n < 0:    # при ошибочном вводе отрицательно числа берется его значеие по абсолютной величине
                n *= (-1)
            Flagin = True

# Если полученный ввод не число, будет вызвано исключение
        except ValueError:
            # Цикл будет повторяться до правильного ввода
            print("Error! Это не число, попробуйте снова.")

        # При успешном преобразовании в целое число,
        # цикл закончится.
        except EOFError:
            print("EOFError! Выходим из меню...")
            FlagProgTermination = False
            break
        else:
            if n > 7 or n == 0:
                print("Error! Допустимые значения от 1 до 7, попробуйте снова.")
            else:
                return n

# End of salute

#   print(salute())


def input_contact():
    name = ""
    name = input("Name: ")
    if len(name) < 2:
        input("Поле Фамилия является обязательным для ввода а длина значения не может быть меньше 2 символов!!!!")
        return name
    else:
        return name + ";" + input("FirstName: ") + ";" + input("Patronimic: ") + ";" + input("PhoneNo: ")
#   return [input('Введите имя: ')+" ", input('Введите фамилию: ')+" ", input('Введите отчество: ')+" ", input('Введите телефон: ') + "\n"]


def inp_newdata_contact(name, line_number):
    #
    print("Введите новые значения имени, отчества или номера телефона")
    print(">>>>-------->>>>>------->>>>>")
    try:
        return name + ";" + input("FirstName: ") + ";" + input("Patronimic: ") + ";" + input("PhoneNo: ") + ";" + str(line_number)
    except EOFError:
        pass
    else:
        pass


def inp_seek_contact():
    try:
        name = input('Ищем по фамилии (на вхождение введенной строки): ')
    except EOFError:
        name = ""  # чтобы присвоить тип name, 'NoneType' has no len()
     #       input("EOFError! Для продолжения нажмите клавишу Enter...")
    else:
        pass
    return name


def inp_delete_contact():
    try:
        name = input('Введите фамилию удаляемого контакта: ')
    except EOFError:
        name = ""  # чтобы присвоить тип name, 'NoneType' has no len()
     #       input("EOFError! Для продолжения нажмите клавишу Enter...")
    else:
        pass
    return name


def inp_update_contact():
    try:
        name = input('Введите фамилию изменяемого контакта: ')
    except EOFError:
        name = ""  # чтобы присвоить тип name, 'NoneType' has no len()
     #       input("EOFError! Для продолжения нажмите клавишу Enter...")
    else:
        pass
    return name
