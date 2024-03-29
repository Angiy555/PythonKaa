#Задача 29
"""
Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.
"""
import os
os.system('CLS')
import time
start = time.perf_counter()
#print(start)

#Пример Вани
n = int(input("Введите числа: "))
max_number = n
while n != 0:
    n = int(input("Введите следующее число: "))
    if max_number < n:
        max_number = n
print(f"Максимальное значение до 0 равно: {max_number}")
stop = time.perf_counter()
print(stop - start)

#Второй вариант
# Яна:
# import random
# sequence = [random.randint(0,20) for _ in range(10)]
# print(sequence)
# max_value = 0 
# found_zero = False

# for num in sequence:
#     if sequence[0] == 0:
#         print("0 находится на 1 месте в последовательности, максимального числа до него нет")
#         found_zero = True
#         break
#     if num == 0:
#         print("Наибольшее значение, завершающееся первым встретившимся нулем:", max_value)
#         found_zero = True
#         break
#     elif num > max_value:
#         max_value = num

# if found_zero == False:
#     print("В последовательности нет нуля")