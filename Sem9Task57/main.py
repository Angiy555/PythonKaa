#задание 57
"""
1. Прочесть с помощью pandas файл
california_housing_test.csv, который находится в папке
sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы
"""

import pandas as pd
import os

os.system('CLS')

file = 'california_housing_train.csv'

df = pd.read_csv(file)

#print(df.head())
#print(df['median_house_value'].max())
#print(df['median_house_value'].min())
#print(df['median_house_value'].mean())#среднее значение
#print(df['median_house_value'].median())#медианное значение
#print(df.median_income == 3.1250)
#print(df.loc[df.median_income == 3.1250,['median_income']].shape)
#print(df.loc[df.median_income == 3.1250,['median_house_value']].max())
#print(df.median_house_value.min())
#print(df.loc[df.median_house_value == df.median_house_value.min(),['median_house_value','population']])
#print(df.loc[df.median_house_value == df.median_house_value.quantile(0.15),['median_house_value','population']])
print(df.median_house_value.quantile(0.01))