import pandas as pd
import configparser


class IncomingTable:
    """ Создание таблицы из файла .xls.
     path - путь и название файла.
     get_table - возвращает таблицу из файла."""

    def __init__(self, path):
        self.__name_seller = None
        self.__path = path
        self.__table = self.processing()

    def get_table(self):
        return self.__table

    def processing(self):
        self.assign_name()
        return pd.read_excel(self.__path)

    def assign_name(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        table_in = pd.read_excel(self.__path)
        str_in = ''.join(table_in.columns)
        for seller in config['compare']:
            if config['compare'][seller] == str_in:
                self.__name_seller = seller
            pass
        # sellers = [seller for seller in config['compare'] if config['compare'][seller] == str_in]
        # print(sellers)
