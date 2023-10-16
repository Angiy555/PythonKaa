#Задание 11
"""
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
"""
import os
os.system('CLS')
num = int(input("Введите неотрицательное число: "))
ferstNum = 1
secondNum = 0
i = 1
fibonachiNum = 0

while i <= num + 1:
    if fibonachiNum == num:
        break
    fibonachiNum = ferstNum + secondNum
    ferstNum = secondNum
    secondNum = fibonachiNum
    i += 1
else:
    i = -1
print(i)