#Задание 41
"""
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
"""
import os
import random
os.system('CLS')

def create_random_list(number):
    return [random.randint(1,10) for _ in range(number+1)]

def count_list_num(list1):
    count = 0
    for i in range(1, len(list1) - 1):
        if list1[i-1] < list1[i] and list1[i] > list1[i + 1]:
            count += 1
    return count

n = int(input("Введите количество элементов массива: "))
list1 = create_random_list(n)
print(list1)
print(count_list_num(list1))