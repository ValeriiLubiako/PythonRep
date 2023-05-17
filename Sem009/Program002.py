#   Задача 42: Узнать какая максимальная households в зоне минимального значения population.
#
#  ссылка на collab (на эту задачу):
#  https://colab.research.google.com/drive/1cy4B-3peyRjmzBCYh__1AcTPNx8_r78N?usp=sharing#scrollTo=SgT-W4WFWgji
#
#   или общая на раздел:
#  https://colab.research.google.com/drive/1cy4B-3peyRjmzBCYh__1AcTPNx8_r78N?usp=sharing
#
import pandas as pd
c = pd.read_csv('sample_data/california_housing_train.csv')   #  считываем файл

# отбираем  записи в соответствии с заданным критерием поиска - минимальным значением в столбце 'population'
# 
d = c[c['population']==c['population'].min()]
# среди отобранных записей находим запись (записи) с максимальн значение в колонке 'households'
print(d['households'].max())
#
#
# Можно не расписывать промежуточные вычисления и записать в блее компактной форме
#
import pandas as pd  #   подгружаем библиотеку pandas
c = pd.read_csv('sample_data/california_housing_train.csv')
print(c[c['population']==c['population'].min()]['households'].max())
#
