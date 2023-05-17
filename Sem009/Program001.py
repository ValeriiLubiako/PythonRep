# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. 
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).
#
#  ссылка на collab:
#  https://colab.research.google.com/drive/1cy4B-3peyRjmzBCYh__1AcTPNx8_r78N?usp=sharing
#
import pandas as pd  #   подгружаем библиотеку pandas
a = pd.read_csv('sample_data/california_housing_train.csv')   #  считываем файл
#  выделяем столбец "средняя стоимость жилья", значения отобраны в соответствии с заданными в задаче условиями
#  на  population, получили 1601 запись
b = a[(a['population']<500) & (a['population']>0)]['median_house_value']
# вычисляем среднее значение по столбцу
print(b.mean())

# Можно не расписывать промежуточные вычисления и записать в блее компактной форме

import pandas as pd  #   подгружаем библиотеку pandas
a = pd.read_csv('sample_data/california_housing_train.csv')   #  считываем файл
print(a[(a['population']<500) & (a['population']>0)]['median_house_value'].mean())
