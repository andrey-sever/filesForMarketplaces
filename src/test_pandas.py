import random
from time import time

import pandas as pd
import xlrd
import openpyxl

# # Открытие xls файла
# df_data = pd.read_excel('data_in/Прайс Алимат.xls')

# # Инфо датафрейма
# df_data.info()

# # Выбор по строкам и столбцам
# print(df_data.iloc[4, 8])

# # Статистика по числовым столбцам
# df_data.describe()

# # Список заголовков столбцов листа
# list_titles = df_data.columns
# print(list_titles)

# # Данные столбца
# data_row = df_data['Название'] # или data_row = df_data.Контрагент
# print(data_row)

# # Удаление столцов
# del_list = ['Дата','Номер','Вид документа', 'Вид операции', 'Информация', 'Организация',
#             'Ответственный', 'Комментарий']
# for i in del_list:
#     del df_data[i]
# print(df_data.head())

# Открытие xlsx файла через xlrd
# file_XLRD = xlrd.open_workbook('data_in/testPandas.xlsx', formatting_info=True)
# df_data = pd.read_excel(file_XLRD)
# print(df_data.head())

# Открытие xlsx файла через openpyxl
# file_openpyxl = openpyxl.load_workbook('data_in/testPandas.xlsx')
# df_data = pd.read_excel(file_openpyxl)
# print(df_data.head())

sheet_witch_zero = [random.randint(0, 9) for i in range(10000)]
# sheet_witch_zero = [7, 0, 2, 9, 0, 3, 1, 0, 5]

print(f'До: {sheet_witch_zero}')

start = time()

# # №2
# count_zero = 0
# while True:
#     try:
#         sheet_witch_zero.remove(0)
#         count_zero += 1
#     except Exception:
#         break
# new_sheet = sheet_witch_zero.copy()
# for i in range(count_zero):
#     new_sheet.append(0)

# №1
new_sheet = []
count_zero = 0
for i in sheet_witch_zero:
    if i == 0:
        count_zero += 1
    else:
        new_sheet.append(i)
for i in range(count_zero):
    new_sheet.append(0)

# # №3
# count_zero = 0
# for i, value in enumerate(sheet_witch_zero):
#     if value == 0:
#         del sheet_witch_zero[i]
#         count_zero += 1
# for i in range(count_zero):
#     sheet_witch_zero.append(0)
# new_sheet = sheet_witch_zero.copy()

finish = time()
print(f'Время затрачено: {finish - start}')

print(f'После: {new_sheet}')