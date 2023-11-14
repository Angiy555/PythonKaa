#Задание 32
"""
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
"""
import os
import random
os.system('CLS')

def create_random_list(number):
    return [random.randint(-10,10) for _ in range(number)]

n = int(input("Введите количество элементов массива: "))
_min = int(input("Введите минимальное значение: "))
_max = int(input("Введите максимальное значение: "))

list1 = create_random_list(n)
print(list1)
list2 = []
for i in range(len(list1)):
    if _min <= list1[i] and list1[i]<= _max:
        list2.append(i)
print(list2)