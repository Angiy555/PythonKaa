#Задание 15
"""
Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
"""
import os
os.system('CLS')
import random
num = int(input("Введите число N арбузов: "))
max = 0
min = 999
for i in range(num):
    mass = random.randint(1,10)
    print(mass, end = ' ')
    if mass <= min:
        min = mass
    if mass >= max:
        max = mass
print()
print(f"Самый тяжелый арбуз весит: {max}")
print(f"Самый легкий арбуз весит: {min}")