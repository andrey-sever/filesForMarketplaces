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
        self.required_columns()
        self.rename_columns()
        self.final_price()

    def assign_name(self):
        str_in = ''.join(self.__table.columns)
        for key in self.__config['compare']:
            if self.__config['compare'][key] == str_in:
                self.__name_seller = key
                break

    def required_columns(self):
        self.__table = self.__table[list(self.__config['columns'][self.__name_seller].split(','))]

    def rename_columns(self):
        if self.__name_seller in self.__config['columns.rename']:
            self.__table.columns = list(self.__config['columns.rename'][self.__name_seller].split(','))

    def final_price(self):
        column_name_price = self.__config['price']['name']
        ratio = float(self.__config['price']['ratio'])
        self.__table[column_name_price] = self.__table[column_name_price] * ratio
