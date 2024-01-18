from tables.incomingTable import IncomingTable
import tables.utilities_tables as tables
import os
import configparser

from tables.utilities_tables import merge_tables

config = configparser.ConfigParser()
config.read('incoming.ini', encoding='utf-8')


def get_working_table():
    list_tables = []
    path = config['other']['path'] + '/'
    for filename in os.listdir(path):
        if filename.endswith('.xls'):
            incTable = IncomingTable(f'{path}{filename}')
            table = incTable.get_table()
            if table is not None:
                list_tables.append(table)  # сохранить в список
                # print(f'{incTable.get_name_seller()}: {table.columns}')
                # print(table.info)
    return merge_tables(list_tables)

# for key in config['compare']:
#     print(key + ': ' + config['compare'][key])

# key = [key for key in config['compare'] if config['compare'][key] == str_in]
