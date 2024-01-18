import pandas as pd
import configparser
from datetime import date


class PatternTable:
    """
    Файл-шаблон в DataFrame
    :name имя объекта, назначается из названия файла
    :matcing - соответсвие столбцов: Остаток, цена
    """
    NAME_CONF_FILE = 'pattern.ini'

    def __init__(self, path):
        self.__path = path
        self.__config = configparser.ConfigParser()
        self.__config.read(PatternTable.NAME_CONF_FILE, encoding='utf-8')
        self.__df = pd.read_excel(path)
        self.__name = None
        self.__matching = None
        self.__name_out = None
        self.processing()

    def get_table(self):
        return self.__df

    def get_name(self):
        return self.__name

    def get_matching(self):
        return self.__matching

    def get_name_out(self):
        return self.__name_out

    def processing(self):
        self.assign_name()
        if self.__name is None:
            self.__df = None
            return
        self.assign_matching()
        self.assign_name_out()

    def assign_name(self):
        """
        Назначение имени объекту из файла ini
        """
        for key in self.__config['names']:
            if self.__config['names'][key].lower() in self.__path.lower():
                self.__name = key
                break

    def assign_matching(self):
        """
        Назначение соответсвия столбцов: Остаток, цена. Тип словарь
        """
        for key in self.__config['column.matching']:
            if key == self.__name:
                self.__matching = eval(self.__config['column.matching'][key])

    def assign_name_out(self):
        self.__name_out = f'{self.__name}_{str(date.today())}'