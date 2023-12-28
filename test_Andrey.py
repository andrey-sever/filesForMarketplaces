from prog.incomingTable import IncomingTable
import os
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

for filenamme in os.listdir(config['DEFAULT']['path'] + '/'):
    if filenamme.endswith('.xls'):
        table = IncomingTable(f'data_in/{filenamme}').get_table()
        print (''.join(table.columns))