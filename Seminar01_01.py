# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
n = int(input("Введите трехзначное число"))
a = n // 100
b = n // 10 % 10
c = n % 10
print(a + b + c)