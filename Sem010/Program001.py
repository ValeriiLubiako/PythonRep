#   Задание 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
#   Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
#
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head() 
#  
#  ссылка на collab (на эту задачу):
#  https://colab.research.google.com/drive/1cy4B-3peyRjmzBCYh__1AcTPNx8_r78N?usp=sharing#scrollTo=1PV-Ve_tUBI_
#
#   или общая на раздел:
#  https://colab.research.google.com/drive/1cy4B-3peyRjmzBCYh__1AcTPNx8_r78N?usp=sharing
#
#
import pandas as pd  # подключаем библиотеки pandos и random
import random
lst = ['robot'] * 10    #  присваиваем 10-ти первым (с 0 по 9) значениям списка lst значение 'robot'
lst += ['human'] * 10   #  добавляем в список lst еще 10 элементов (с 10 по 19) и присваиваем им значение 'human'
random.shuffle(lst)   #  сформировали список lst из 20 случайным образом чередующихся значений 'robot' и 'human'
data = pd.DataFrame({'whoAmI':lst})    # поcтроили на основе lst DataFrame, состоящий из одного столбца с заголовком 'whoAmI'
# и значениями из списка lst (19 "строк")
data.head()  # смотрим, что получилось....

# whoAmI
# 0	robot
# 1	human
# 2	human
# 3	robot
# 4	human

# строим список с заголовками для результирующего one-hot фрейма
# берем уникальные значения из построенного одностолбцового фрейма
unique_vals=data['whoAmI'].unique()
print(unique_vals)  #  смотрим, что получилось

#    array(['robot', 'human'], dtype=object)

#    создаем фрейм (DataFrame) one_hot_data, столбцам присваиваем названия из полученного выше списка unique_vals
one_hot_data = pd.DataFrame(columns=unique_vals)
print(one_hot_data)  #  проверяем что получилось

#   robot	human

#  в цикле заполняем значения столбцов фрейма one-hot_data
for val in unique_vals:
    one_hot_data[val] = (data['whoAmI'] == val)
print (one_hot_data)   #   смотрим результат

# 	    robot	human
# 0	    True	False
# 1	    False	True
# 2	    False	True
# 3	    True	False
# 4	    False	True
# 5	    False	True
# 6	    True	False
# 7	    False	True
# 8	    True	False
# 9	    False	True
# 10	True	False
# 11	True	False
# 12	False	True
# 13	True	False
# 14	False	True
# 15	False	True
# 16	True	False
# 17	False	True
# 18	True	False
# 19	True	False

#  преобразуем значения к типу integer и смотри результат - True и False заменились на 1 и 0

one_hot_data.astype(int)
print(one_hot_data)

# 	robot	human
# 0	    1	    0
# 1	    0	    1
# 2	    0	    1
# 3	    1	    0
# 4	    0	    1
# 5	    0	    1
# 6	    1	    0
# 7	    0	    1
# 8	    1	    0
# 9	    0	    1
# 10	1	    0
# 11	1	    0
# 12	0	    1
# 13	1	    0
# 14	0	    1
# 15	0	    1
# 16	1	    0
# 17	0	    1
# 18	1	    0
# 19	1	    0

#  можем записать более компактно, обьединить построение фрейма с изменением типа значений его элементов на int
for val in unique_vals:    #  в цикле заполняем значения столбцов one-hot DataFrame и меняем тип значений на int
  one_hot_data[val] = (data['whoAmI'] == val).astype(int)
print(one_hot_data)

# 	robot	human
# 0	    1	    0
# 1	    0	    1
# 2	    0	    1
# 3	    1	    0
# 4	    0	    1
# 5	    0	    1
# 6	    1	    0
# 7	    0	    1
# 8	    1	    0
# 9	    0	    1
# 10	1	    0
# 11	1	    0
# 12	0	    1
# 13	1	    0
# 14	0	    1
# 15	0	    1
# 16	1	    0
# 17	0	    1
# 18	1	    0
# 19	1	    0