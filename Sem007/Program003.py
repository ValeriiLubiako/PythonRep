#  Демонстрация использованя библиотеки timeit 
#  для определения времени выполнения кода
#
#   Каждое представление списков в Python включает три элемента:
#   1. expression — какое-либо вычисление, вызов метода или любое другое допустимое выражение,
#       возвращающее значение. В приведенном выше примере выражение i * i является квадратом
#       значения члена.
#   2. member является объектом или значением в списке или итерируемом объекте (iterable). 
#       В приведенном выше примере значением элемента является i.
#   3. iterable — список, множество, последовательность, генератор или любой другой объект, который
#       который может возвращать свои элементы по одному. В приведенном выше примере iterable — это range(10).
#     new_list = [expression for member in iterable (if conditional)]   
#
import random
import timeit
TAX_RATE = .08
txns = [random.randrange(100) for _ in range(100000)]
def get_price(txn):
    return txn * (1 + TAX_RATE)

def get_prices_with_map():
    return list(map(get_price, txns))
def get_prices_with_comprehension():
    return [get_price(txn) for txn in txns]

def get_prices_with_loop():
    prices = []
    for txn in txns:
        prices.append(get_price(txn))
    return prices

print(timeit.timeit(get_prices_with_map, number=100))
# 2.0554370979998566
print(timeit.timeit(get_prices_with_comprehension, number=100))
# 2.3982384680002724
print(timeit.timeit(get_prices_with_loop, number=100))
# 3.0531821520007725import random