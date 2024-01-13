from tables.incomingTable import IncomingTable
import os
import configparser

from tables.utilities_tables import merge_tables

config = configparser.ConfigParser()
config.read('incoming.ini', encoding='utf-8')

list_tables = []
path = config['other']['path'] + '/'
for filename in os.listdir(path):
    if filename.endswith('.xls'):
        incTable = IncomingTable(f'{path}{filename}')
        table_df = incTable.get_table_df()
        list_tables.append(table_df) #сохранить в список
        print(f'{incTable.get_name_seller()}: {table_df.columns}')
        print(table_df.info)
newTable = merge_tables(list_tables)                    #
newTable.to_excel('/home/andrey/new_table.xlsx', index=False)    # Соединенные таблицы и сброс в excel
print(newTable.info)                                    #

# for key in config['compare']:
#     print(key + ': ' + config['compare'][key])

# key = [key for key in config['compare'] if config['compare'][key] == str_in]