#Задача 25
"""
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
"""
import os
os.system('CLS')

input_list = "a a a b c a a d c d d"
user_list = input_list.split()
res_list = []
#print(user_list[:3].count('a'))
for i in range(len(user_list)):
    tmp = user_list[:i].count(user_list[i])
    if tmp >= 1:
        res_list.append(f'{user_list[i]}_{tmp}')
    else:
        res_list.append(user_list[i])
print(input_list)
print(" ".join(res_list))

#Второй способ
# strint_part = "a a a b c a a d c d d"
# sting_array = strint_part.split()
# string_dict = dict()
# zero = ""
# for i in sting_array:
#     if i in string_dict:
#         string_dict[i] += 1
#         zero += f"{i}_{string_dict[i]} "
#     else:
#         string_dict[i] = 0
#         zero += f"{i} "
# print(zero)