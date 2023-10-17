#Задание 14
"""
Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N.
"""
import os
os.system('CLS')

num = int(input("Введите целое число N: "))
p = 2
for i in range(num):
    x = p ** i
    if x < num:
        print(x, end = ' ')
    else:
        break