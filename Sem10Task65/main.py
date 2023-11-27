#Задание 65
"""
Написать EDA для датасета про пингвинов
Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя
аргументы hue, size, stile
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить Heatmap
● Использовать 2-3 гистограммы
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
file = 'penguins.csv'

penguins = pd.read_csv(file)

sns.boxplot(data=penguins, x='species', y='bill_length_mm')
sns.displot(data=penguins, x="flipper_length_mm", hue="species", col="species")


#penguins.groupby(['species', 'sex']).mean()


penguins.loc[penguins.bill_length_mm >= 42, 'bill_group'] = 'High'
penguins.loc[(penguins.bill_length_mm >35) & (penguins.bill_length_mm < 42), 'bill_group'] = 'Middle'
penguins.loc[penguins.bill_length_mm <= 35, 'bill_group'] = 'Low'
penguins.head()


sns.histplot(data=penguins, x='flipper_length_mm', hue='bill_group', multiple="stack")

sns.PairGrid(penguins, hue='species').map(sns.scatterplot).add_legend()

plt.show()