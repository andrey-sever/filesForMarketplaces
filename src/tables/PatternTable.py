import pandas as pd
import configparser



class PatternTable:
    """
    Файл-шаблон в DataFrame
    :name имя объекта, назначается из названия файла
    """
    NAME_CONF_FILE = 'pattern.ini'

    def __init__(self, path):
        self.__config = configparser.ConfigParser()
        self.__config.read(PatternTable.NAME_CONF_FILE, encoding='utf-8')
        self.__df = pd.read_excel(path)
        self.__name = None
        self.processing()

    def get_table(self):
        return self.__df

    def processing(self):
        pass

    def assign_name(self):
        """
        Назначение имени объекту
        """