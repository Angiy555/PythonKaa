import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
file = 'california_housing_train.csv'

df = pd.read_csv(file)
# 1. Изобразите отношение households к population с
# помощью точечного графика
sns.scatterplot(data=df, x = 'population', y = 'households')
# 2. Визуализировать longitude по отношения к
# median_house_value, используя линейный график
sns.relplot(x='longitude', y='median_house_value', kind='line', data = df)
# 3. Представить гистограмму по housing_median_age
sns.histplot(data = df, x = 'housing_median_age')
# 4. Изобразить гистограмму по median_house_value с
# оттенком housing_median_age
df.loc[df['housing_median_age'] > 10, 'income_group'] = 'old'
df.loc[df['housing_median_age'] < 10, 'income_group'] = 'new'
sns.displot(data = df, x = 'median_house_value', hue='income_group')

plt.show()
