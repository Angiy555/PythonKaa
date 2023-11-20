#Задание 36
"""
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
ровно два аргумента, как, например, у операции умножения.
"""
import os
os.system('CLS')

def print_operation_table(operation, num_Rows, num_Columns):    
    if num_Rows > 1 and num_Columns > 1:        
        print(' '.join([str(k) for k in range(1, num_Columns + 1)]))
        for i in range(2, num_Rows + 1):
            s = ' '.join([str(operation(i, j)) for j in range(2, num_Columns + 1)])
            print(str(i) + " " + s)
    else:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")

print_operation_table(lambda x, y: x * y, 3, 3)