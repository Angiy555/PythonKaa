#Задание 21
"""
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
import os
os.system('CLS')
#Первый способ
user_list_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]

list_res = []
for i in user_list_dict:
    for j in i:
        if i[j].strip() not in list_res:
            list_res.append(i[j].strip())
print(f"Все уникальные: {list_res}")

#Второй способ
user_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}] 
result = set(v.strip() for i in user_list for v in i.values())
print(result)

