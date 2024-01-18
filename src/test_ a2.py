import os
import configparser
from src.tables.PatternTable import PatternTable
from src.tables.utilities_tables import add_balance_price
from src.test_Andrey import get_working_table

config = configparser.ConfigParser()
config.read('pattern.ini', encoding='utf-8')

path = config['other']['path'] + '/'
for filename in os.listdir(path):
    if filename.endswith('.xlsx'):
        pattTable = PatternTable(f'{path}{filename}')
        table = pattTable.get_table()
        if table is not None:
            working_table = get_working_table()
            add_balance_price(pattTable, working_table)
