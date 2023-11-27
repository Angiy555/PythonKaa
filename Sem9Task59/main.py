#Задание 59
"""
1. Проверить есть ли в файле пустые значения
2. Показать median_house_value где median_income < 2
3. Показать данные в первых 2 столбцах
4. Выбрать данные где housing_median_age < 20 и
median_house_value > 70000
"""
import os

os.system('CLS')

import pandas as pd
# california_housing_train.csv
file = 'california_housing_train.csv'

# Задача №57. Решение в группах
# 1. Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
df = pd.read_csv(file)

print(df.head())
print(df.tail())
# 2. Посмотреть сколько в нем строк и столбцов
print(df.shape)
# 3. Определить какой тип данных имеют столбцы
print(df.dtypes)


# Задача №59. Решение в группах
# 1. Проверить есть ли в файле пустые значения
print(df.isnull().sum())
# 2. Показать median_house_value где median_income < 2
print(df.loc[df.median_income < 2, ['median_income', 'median_house_value']])
# 3. Показать данные в первых 2 столбцах
print(df[['longitude', 'latitude']])
print(df.iloc[:, 0:2])
# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000
print(df.loc[df.housing_median_age < 20, ['housing_median_age', 'median_house_value']])
# [4826 rows x 2 columns]
print(df.loc[(df.housing_median_age < 20) & (df.median_house_value > 70000), ['housing_median_age', 'median_house_value']])
    

# df.to_excel('file.xlsx')
# print('*' * 25)
# df2 = df.iloc[:, 0:2]
# print(df2.head())
# print(df2.shape)
# df2.to_excel('file2.xlsx')
# df2.to_csv('df2.csv')

# Задача №61. Решение в группах
# 1. Определить какое максимальное и минимальное значение median_house_value
# print(df.median_house_value.max())
print(df[['median_house_value']].max())
print(df[['median_house_value']].min())
print(df[['median_house_value']].mean())  # среднее
print(df[['median_house_value']].median())  # медианное


# 2. Показать максимальное median_house_value, где median_income = 3.1250
print(df.loc[df.median_income == 3.1250, ['median_house_value']].max())

# 3. Узнать какая максимальная population в зоне минимального значения median_house_value
print(df.median_house_value.min())  # 14999.0
# min_ = df.median_house_value.min()
print(df.loc[df.median_house_value == df.median_house_value.min(), ['median_house_value', 'population']])
# df.loc[df.median_house_value == df.median_house_value.quantile(0.15)]
print('median_house_value.quantile:')
print(df.median_house_value.quantile(0.05))
print(df.loc[df.median_house_value < df.median_house_value.quantile(0.05), ['median_house_value', 'population']])
df_min_val = df.loc[df.median_house_value < df.median_house_value.quantile(0.05)]
print(df_min_val.population.max())