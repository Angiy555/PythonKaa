#Задание 6
"""
Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.
"""
import os
os.system('CLS')
num = int(input("Введите шестизначное число: "))
numL = num//1000
byfL = 0
byfR = 0
r = range(0,3,1)
if 1000000>num>99999:
    for i in r:
        byfL = byfL + num%10
        num = num//10
        byfR = byfR + numL%10
        numL = numL//10
    if byfL == byfR:
        print("Вы ввели номер счастливого билета!!!")
    else:
        print("Вы ввели номер не счастливого билета.")
else:
    print("Введено не шестизначное число")