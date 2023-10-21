#Задание 18
"""
Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка содержит число X
"""
import os
import random
os.system('CLS')
n = int(input("Введите количество элементов в массиве: "))
list_n = []
for i in range(n):
    list_n.append( random.randint(0,10))
print(list_n)
x = int(input("Введите искомое число в массиве: "))
byf = abs(x - list_n[0])
nearest_num = list_n[0]
for i in range(1,len(list_n)):
    if byf > abs(x - list_n[i]):
        byf = abs(x - list_n[i])
        nearest_num = list_n[i]
print(f"Ближайшее к искомому числу {x} является число {nearest_num}")