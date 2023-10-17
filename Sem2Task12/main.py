#Задание 12
"""
Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
import os
os.system('CLS')

x = int(input("Введите натуральное число X от 1 до 1000: "))
y = int(input("Введите натуральное число Y от 1 до 1000: "))
if x < 1 or x > 1000 or y < 1 or y > 1000:
    print("Вы ввели число не из заданного диапазона!")
else:
    s = x + y
    p = x * y
    print(f"Сумма X и Y равна: {s}")
    print(f"Произведение X и Y равно: {p}")
    stop = 0
    for i in range(1001):
        if stop != 1:
            for j in range(1001):
                if stop != 1:
                    if i * j == p and i + j == s:
                        print(f"Искомое X равно: {i}, искомое Y равно: {j}")
                        stop = 1
                              