from prog.incomingTable import IncomingTable
import os
import configparser


config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

path = config['other']['path'] + '/'
for filenamme in os.listdir(path):
    if filenamme.endswith('.xls'):
        incTable = IncomingTable(f'{path}{filenamme}')
        table = incTable.get_table()
        print(f'{incTable.get_name_seller()}: {table.columns}')
        print(table.head())

# for key in config['compare']:
#     print(key + ': ' + config['compare'][key])

# key = [key for key in config['compare'] if config['compare'][key] == str_in]