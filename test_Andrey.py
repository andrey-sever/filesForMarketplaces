from prog.incomingTable import IncomingTable
import os
import configparser


config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

for filenamme in os.listdir(config['other']['path'] + '/'):
    if filenamme.endswith('.xls'):
        table = IncomingTable(f'data_in/{filenamme}').get_table()
        print(''.join(table.columns))
        print(table.get_name_seller)

# for key in config['compare']:
#     print(key + ': ' + config['compare'][key])

# key = [key for key in config['compare'] if config['compare'][key] == str_in]