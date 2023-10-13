#Задание 2
#Найдите сумму цифр трехзначного числа.
import os
os.system('CLS')
num = int(input("Введите трехзначное число: "))
byf = 0
while num >0:
    byf = byf + num%10
    num = num//10
print(f"Сумма цифр числа равна: {byf}")