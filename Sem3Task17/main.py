#Задание 17
"""
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
"""
import os
os.system('CLS')
list_num = [1,1,2,0,-1,3,4,4]
#print(len(set(list_num)))
#print(set(list_num))

new_list = []
for i in list_num:
    if i not in new_list:
        new_list.append(i)
print(len(new_list))
print(new_list)
