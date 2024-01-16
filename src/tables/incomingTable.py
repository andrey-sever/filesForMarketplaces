import pandas as pd
import configparser


class IncomingTable:
    """
    Создание таблицы типа DataFrame из файла .xls.
    Остаются нужные столбцы с переименованием.
    Данные для таблицы в ini файле NAME_CONF_FILE
    path - путь и название файла.
    name_seller - поставщик.
    get_table_df - возвращает таблицу DataFrame из файла.
    get_name_seller - возвращает название поставщика.
    """
    NAME_CONF_FILE = 'incoming.ini'

    def __init__(self, path):
        self.__config = configparser.ConfigParser()
        self.__config.read(IncomingTable.NAME_CONF_FILE, encoding='utf-8')
        self.__df = pd.read_excel(path)
        self.__name_seller = None
        self.processing()

    def get_table(self):
        return self.__df

    def get_name_seller(self):
        return self.__name_seller

    def processing(self):
        self.assign_name()
        if self.__name_seller is None:
            self.__df = None
            return
        self.required_columns()
        self.rename_columns()
        self.final_price()

    def assign_name(self):
        """
        Назначение имени поаставщика объекту
        """
        str_in = ''.join(self.__df.columns)
        for key in self.__config['compare']:
            if self.__config['compare'][key] == str_in:
                self.__name_seller = key
                break

    def required_columns(self):
        """
        Оставляет нужные столбцы
        """
        self.__df = self.__df[list(self.__config['columns'][self.__name_seller].split(','))]

    def rename_columns(self):
        """
        Переименовывает столбцы
        """
        if self.__name_seller in self.__config['columns.rename']:
            self.__df.columns = list(self.__config['columns.rename'][self.__name_seller].split(','))

    def final_price(self):
        """
        Изменение столбца цен на коэффициент
        Пример: 0.5, 1.3
        """
        column_name_price = self.__config['price']['name']
        ratio = float(self.__config['price']['ratio'])
        self.__df[column_name_price] = self.__df[column_name_price] * ratio

#ToDo: path подумать откуда брать, можтет общий ini, или из своего ini