# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
#
# Пример
#
# Ввод: 5
# Ввод: 1 4 1 2 5 8
# вод: 6
# -> 5
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
                        narray = list()
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
                narray = list()
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

        n = int(input("Введите значение числа X (выход - Ctrl-Z + Enter): "))


# Если полученный ввод не число, будет вызвано исключение
    except ValueError:
        # Цикл будет повторяться до правильного ввода
        print("Error! Это не число, попробуйте снова.")

        # При успешном преобразовании в целое число
        # цикл закончится.
    except EOFError:
        print("EOFError! Выходим из цикла ввода.")
        FlagProgTermination = False
        break
    else:

        diff = abs(n - narray[0])  # абсолютная величина разницы
        k = narray[0]
        for i in range(1, len(narray)):
            if diff > abs(narray[i] - n):
                diff = abs(narray[i] - n)
                k = narray[i]
        print("Самый близкий по величине элемент к заданному числу X: ", k)
