# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума
# и не больше заданного максимума)
# 
#
#
#
# from random import random, randrange, randint
import random

arraylen = int(input("Введите длину массива: "))

minArrVal = int(input("Введите нижнюю границу значений: "))
maxArrVal = int(input("Введите верхнюю границу значений: "))

list_1 = []
for i in range (arraylen):
    list_1.append(random.random()*2000-1000)

print (*list_1)

list_2 = []
for x in list_1:
    if x >= minArrVal or x<= maxArrVal:
        list_2.append(x)
        
print("Массив значений, попадающих в интервал от ")
print (minArrVal, "до ",maxArrVal, ":"  )
print[*list_2]