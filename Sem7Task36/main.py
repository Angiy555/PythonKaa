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

#Вариант 2
def print_operation_table_2(operation, num_rows, num_columns):
    if num_rows < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in range(1,num_rows+1):
            if i == 1:
                sq = [i for i in range(1,num_rows+1)]
            else:
                sq = [operation(i,j) if j > 1 else i for j in range(1, num_columns + 1)]
            print(*sq)

print_operation_table(lambda x, y: x * y, 3, 3)
print_operation_table_2(lambda x, y: x * y, 3, 3)