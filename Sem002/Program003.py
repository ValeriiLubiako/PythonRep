# Задача 14: Требуется вывести все целые (неотрицательные) степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 
# Возведение в степень будем вычислять как произведение числа само на себя число раз,
# равное показателю степени (из определения возведения в степень)
# Начнем с показателя степени 0, 2 в нулевой степени равно 1.
# Следующее значение (k+1) получается путем умножения текущего значения произведения (2**k) на 2.
#  Значение 2**k накапливается в переменной m

n = int(input("Введите максимально допустимое значение: "))
m = 1
while m <=n:
    print(m)
    m = m*2