#Задание 33
"""
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""
import os
os.system('CLS')
def change_num(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    for n in range(len(numbers)):
        if numbers[n] == max_num:
            numbers[n] = min_num
numbers = [1, 2, 3, 4, 5]
change_num(numbers)
print(*numbers)

#Второй способ
def grades_correction (array, i, max_num):
    if i == -1:
        return
    if array[i] == max_num:
        array[i] = min(array)
    return grades_correction (array, i - 1, max_num)

array = [1, 3, 3, 3, 4]
grades_correction(array, len(array)-1, max(array))
print(*array)


#Третий способ
vas_marks = [1, 3, 3, 3, 4]
print([min(vas_marks) if i == max(vas_marks) else i for i in vas_marks])