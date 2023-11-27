import pandas as pd
df = pd.read_csv('california_housing_train.csv')

"""
Задача 40: Работать с файлом california_housing_train.csv, 
который находится в папке sample_data. Определить среднюю 
стоимость дома, где кол-во людей от 0 до 500 (population).
"""
avg = (df.loc[(df['population'] > 0) & (df['population'] < 500) , ['housing_median_age'] ].mean()).values[0]
print(avg)
"""
Задача 42: Узнать какая максимальная households в зоне минимального 
значения population.
"""
min_population = df['population'].min()
print(df.loc[(df['population'] == min_population) , ['households'] ].max().values[0])