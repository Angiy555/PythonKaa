#Задание 31
"""
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
"""
import os
os.system('CLS')
def fib(n):
    res =""
    for i in range(1, n+1):
        res += f'{fib(i)} '
    return res
print(fib(int(input("Введите число Фибоначи: "))))