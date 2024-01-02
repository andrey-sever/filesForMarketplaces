import pandas as pd
import xlrd
import openpyxl

# Открытие xls файла
df_data = pd.read_excel('data_in/Прайс Алимат.xls')

# Инфо датафрейма
df_data.info()

# # Выбор по строкам и столбцам
# print(df_data.iloc[4, 8])

# # Статистика по числовым столбцам
# df_data.describe()

# # Список заголовков столбцов листа
# list_titles = df_data.columns
# print(list_titles)

# Данные столбца
data_row = df_data['Название'] # или data_row = df_data.Контрагент
print(data_row)

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

