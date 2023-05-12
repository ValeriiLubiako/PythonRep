#  func.ru

#  import interface


def add_contact(contact):
#    contact = [input('Введите имя: ')+" ", input('Введите фамилию: ')+" ", input('Введите отчество: ')+" ", input('Введите телефон: ')]
    data = open('file.txt', 'a', encoding='utf-8')
    data.writelines(contact)
    # data.write('\n')
    data.close()


def seek_contact(name):
    with open('file.txt', 'r', encoding='utf-8') as contact_list:
        for x in contact_list:
            if name in x:
                print(x)
    contact_list.close()


def print_all():
    contact_list = open('file.txt', 'r', encoding='utf-8')
    num = 1
    for i in contact_list:
        print(f'{num}. {i}')
        num += 1
    contact_list.close()


def del_contact(search):
    contact_list = open('file.txt', 'r', encoding='utf-8')
    cash_list = []
    for i in contact_list:
        if search in i:
            continue
        cash_list.append(i)
    contact_list.close()

    contact_list = open('file.txt', 'w', encoding='utf-8')
    for i in cash_list:
        contact_list.writelines(i)
    contact_list.close()


def change_contact(search):
    contact_list = open('file.txt', 'r', encoding='utf-8')
    cash_list = []
    for i in contact_list:
        if search in i:
            cash_list.append(interface.get_contact())
            continue
        cash_list.append(i)
    contact_list.close()

    # contact_list = open('file.txt', 'w', encoding='utf-8')
    # for i in cash_list:
    #     contact_list.writelines(i)
    # contact_list.close()

