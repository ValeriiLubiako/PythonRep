# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# ПРивер:
# Ввод: 5
# Ввод: 1 5 3 4 2
# Ввод: 3
# -> 1
#
#
Flag = True
Flagin = True
#
narray = list()  # завели числовой массив для хранения чисел, соответствующих веденным в строку цифр
while Flag:
    try:

        cn = input("Введите количество чисел в массиве: ")
        n = int(cn)
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
        while Flagin:

            strtxt = input("Введите " + cn +
                           " элементов массива через пробел: ")
# сформировали символьный список из введенных чисел (последовательностей цифр)
            listarray = strtxt.split()
            if len(listarray) == n:
                Flag = False
                Flagin = False
                for listarrayelement in listarray:   # формируем числовой массив из введенных в строку цифр
                    try:
                        narray.append(int(listarrayelement))
#                   Если полученный ввод не число, будет вызвано исключение
                    except ValueError:
                        # Цикл будет повторяться до правильного ввода
                        print(
                            "Error! Введенный элемент массива - НЕ число, попробуйте снова.")
                        Flagin = True
                        Flag = True
                        break
        # При успешном преобразовании в целое число,
        # цикл закончится.
                    except EOFError:
                        print("EOFError! Выходим из внутреннего цикла ввода.")
                        FlagProgTermination = False
                        break
                    else:
                        Flag = False
                        Flagin = False
            else:
                print("Ошибка при вводе элементов массива")
            Flagin = False
            break
#
print(listarray)
print(len(listarray))
print(narray)
# else:
# print("Принудительное завершение задания (по Ctrl-Z + Enter)")
#
Flag = True
while Flag:
    try:

        n = int(input("Введите значение числа X: "))


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
        print("Найдено значений числа ", n, ": ", narray.count(n))
        Flag = False
