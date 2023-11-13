#задание 39
"""
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
"""
import os
import random
os.system('CLS')

def filter_list(array1, array2):
    res_array = []
    for i in array1:
        if i not in array2:
            res_array.append(i)
    return res_array

def create_random_list(number):
    return [random.randint(-10,10) for _ in range(number+1)]

#Второй способ
def filter_list_2(array1, array2):
    return [i for i in array1 if i in set(array1) - set(array2)]

number_1 = int(input("Введите количество элементов первого массива: "))
int_array_1 = create_random_list(number_1)
print(int_array_1)
number_2 = int(input("Введите количество элементов второго массива: "))
int_array_2 = create_random_list(number_2)
print(int_array_2)
print(filter_list(int_array_1, int_array_2))
print(filter_list_2(int_array_1, int_array_2))