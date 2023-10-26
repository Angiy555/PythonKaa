#Задание 37
"""
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
"""
import os
os.system('CLS')

def reverse_num(num, array):
    if num == 0:
        return
    print(array[num - 1], end = " ")
    return reverse_num(num - 1, array)
reverse_num(3, [3, 4, 5])


#Вариант второй
num = 5

def reverse_output(n, x = None):
    if n > 0:
        x = input("Введите число: ")
        reverse_output(n - 1)
    if x != None:
        print(x, end=" ")

reverse_output(num)

#Третий способ
def rec(n):
    if n == 0:
        return ''
    x = int(input("Введите число: "))
    return f'{rec(n - 1)} {x}'


n = int(input("Введите кол-во чисел: "))
print(rec(n))