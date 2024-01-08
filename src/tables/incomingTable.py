import pandas as pd
import configparser


class IncomingTable:
    """
    Создание таблицы из файла .xls.
    Остаются нужные столбцы с переименованием.
    path - путь и название файла.
    name_seller - поставщик.
    get_table - возвращает таблицу из файла.
    get_name_seller - возвращает название поставщика.
    """

    def __init__(self, path):
        self.__config = configparser.ConfigParser()
        self.__config.read('config.ini', encoding='utf-8')
        self.__table = pd.read_excel(path)
        self.__name_seller = None
        self.processing()

    def get_table(self):
        return self.__table

    def get_name_seller(self):
        return self.__name_seller

    def processing(self):
        self.assign_name()
        if self.__name_seller is None:
            self.__table = None
            return
        self.delete_columns()
        self.rename_columns()

    def assign_name(self):
        str_in = ''.join(self.__table.columns)
        for key in self.__config['compare']:
            if self.__config['compare'][key] == str_in:
                self.__name_seller = key
                break

    def delete_columns(self):
        columns_leave = list(self.__config['columns'][self.__name_seller].split(','))
        columns_file = list(self.__table.columns)
        for i in columns_file:
            if i not in columns_leave:
                del self.__table[i]

    def rename_columns(self):
        if self.__name_seller in self.__config['columns.rename']:
            self.__table.columns = list(self.__config['columns.rename'][self.__name_seller].split(','))

