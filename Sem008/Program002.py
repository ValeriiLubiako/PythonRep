# interface

def salute():
    print("Меню работы с записной книжкой.\n" +
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
            print("EOFError! Выходим из цикла ввода.")
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
    return [input("Name: ") + ";", input("FirstName: ") + ";",
    input("Patronimic: ") + ";", input("PhoneNo: ") + "\n"]
#   return [input('Введите имя: ')+" ", input('Введите фамилию: ')+" ", input('Введите отчество: ')+" ", input('Введите телефон: ') + "\n"]


def get_del_contact():
    return input('Введите фамилию удаляемого контакта: ')


def get_change_contact():
    return input('Введите фамилию изменяемого контакта: ')

