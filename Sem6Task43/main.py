#Задание 43
"""
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
"""
import os
import random
os.system('CLS')

def create_random_list(number):
    return [random.randint(1,10) for _ in range(number)]

def pair_search(list1: list):
    count = 0
    set_list = set(list1)
    for i in set_list:
        count += list1.count(i) // 2
    return count


n = int(input("Введите количество элементов массива: "))
list1 = create_random_list(n)
print(list1)
print(f"В списке {pair_search(list1)} пар")