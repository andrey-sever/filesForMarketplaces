import pandas as pd


class TableDataFrame:
    """ Создание таблицы из файла .xls.
     patch - входной путь и название файла.
     get_table - возвращает таблицу из файла."""
    def __init__(self, path):
        self.__table = pd.read_excel(path)

    def get_table(self):
        return self.__table
