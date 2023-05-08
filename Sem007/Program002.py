# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
# как, например, у операции умножения.
#
# *Пример:*
#
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
#
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36
#
#  В теле функции использованы три цикла
#  В первом цикле формируется первая (заголовочная)  со значениями от 1 до числа столбцов
#  Далее используются два вложенных цикла для формирования значений элементов таблицы
#  согласно параметров, передаваемых функции
#
def print_operation_table(operation, num_rows=6, num_columns=6):
    if num_rows <= 2 or num_columns <= 2:
        print("Предполагается, что число строк или столбцов больше двух...")
    else:
        #        print(" ".join([str(i) for i in range(1, num_columns + 1)]))
        outputline = ""
        for i in range(1, num_columns + 1):
            outputline = outputline + str(i) + "     "
        print(outputline)
        for i in range(2, num_rows + 1):
            print(i, end="     ")
            for j in range(2, num_columns + 1):
                print(operation(i, j), end="     ")
            print()


print_operation_table(lambda x, y: x + y)
