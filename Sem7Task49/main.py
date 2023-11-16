#Задание 49
"""
Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет
самую большую площадь. Напишите функцию
find_farthest_orbit(list_of_orbits), которая среди списка орбит
планет найдет ту, по которой вращается самая далекая
планета. Круговые орбиты не учитывайте: вы знаете, что у
вашей звезды таких планет нет, зато искусственные спутники
были были запущены на круговые орбиты. Результатом
функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего
будет найти эллипс в два шага: сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая
планета ровно одна
"""
import os
from math import pi
os.system('CLS')

#Первый способ
def find_farthest_orbit(list_of_orbits):
    max_el = list_of_orbits[0]
    max_s = 0
    for i in list_of_orbits:
        if i[0] != i[1]:
            if pi * i[0] * i[1] > max_s:
                max_s = pi * i[0] * i[1]  
                max_el = i
    return max_el

#Второй способ
def find_farthest_orbit_1(list_of_orbits):
    res_max = max([pi * i[0] * i[1] for i in list_of_orbits if i[0] != i[1]])
    res = list(filter(lambda x: res_max == pi * x[0] * x[1], list_of_orbits))
    return res[0]

#Третий способ
def find_farthest_orbit_2(list_of_orbits):
    return max(list(filter(lambda x: x[0] != x[1],list_of_orbits)), key = lambda x: pi*x[0]*x[1])

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))
print(find_farthest_orbit_1(orbits))
print(find_farthest_orbit_2(orbits))