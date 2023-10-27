#Задание 28
"""
Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
"""
import os
os.system('CLS')
def recsum(a, b):
    if b == 0:
        return a
    return 1 + recsum(a, b - 1)
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
print(f"Сумма числа {a} и числа {b} равна {recsum(a, b)}")