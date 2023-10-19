#Задание 19
"""
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
"""
import os
os.system('CLS')
k = int(input("Введите смещение элементов вправо: "))
list_num = [1,2,3,4,5,6]
#x = list_num.pop()
#print(x)
print(list_num)
print(list_num[k:] + list_num[:k])#первое решение

for i in range(k):#второе решение
    list_num.insert(0,list_num.pop())
print(list_num)