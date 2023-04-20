# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
#
#
import random
n = int(input("Введите общее количество монет"))
#  Формируем массив coins [n], описывающий лежащие монеты, считаем, что расределение их носит случайгый характер
#  coins [i] = 'eagle' - орел,  coins [i] = 'tails' - решка
coins = []
for i in range (n):
    coins.append("eagle" if random.randint(0,1) == 0   else "tails")
print(coins)   # для проверки распечатаем массив
#
# в цикле по всем элементам сформированного массива coins просчитаем число монет, лежащих орлом (neagle) или решкой (ntails)
#
neagle = 0
ntails = 0
for coin in coins:
    if coin == 'tails':
        ntails += 1
    else:
        neagle += 1
print("ntails=", ntails)        
print("neagle=", neagle)

if ntails > neagle:
    print ("Turn over", neagle, "eagles")
else:
    print ("Turn over", ntails, "tails")