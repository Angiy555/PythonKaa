#задание 35
"""
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""
import os
os.system('CLS')
def prime_num(n):
    if n <= 1:
        return "No"
    for i in range(2, n - 1):
        if n % i == 0:
            return "No"
    return "Yes"
print(prime_num(2))

#Второй способ
def prime_num2(n, i = None):
    if i is None:
        i = n - 1
    if i == 1:
        return "Yes"
    if n <= 1:
        return "No"
    if n % i == 0:
        return "No"    
    return prime_num2(n, i - 1)

print(prime_num2(2))
