#Задание 51
"""
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.
"""
import os
os.system('CLS')

def same_by(characteristic, objects):
    if len(set(map(characteristic, objects))) in (0, 1):
        return True
    return False

values = [0, 2, 10, 6]
print(same_by(lambda x: x % 2, values))