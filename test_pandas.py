import pandas as pd
import xlrd
import openpyxl

# Открытие xls файла
df_data = pd.read_excel('data_in/testPandas.xls')
# Список заголовков столбцов листа
list_titles = df_data.columns.ravel()
print(list_titles)
# Данные столбца
data_row = df_data['Контрагент']
print(data_row)

# Открытие xlsx файла через xlrd
# file_XLRD = xlrd.open_workbook('data_in/testPandas.xlsx', formatting_info=True)
# df_data = pd.read_excel(file_XLRD)
# print(df_data.head())

# Открытие xlsx файла через openpyxl
# file_openpyxl = openpyxl.load_workbook('data_in/testPandas.xlsx')
# df_data = pd.read_excel(file_openpyxl)
# print(df_data.head())

