from prog.tableDataFrame import TableDataFrame

table_one = TableDataFrame('data_in/testPandas.xls').get_table()
table_one.info()
table_two = TableDataFrame('data_in/Прайс Алимат.xls').get_table()
table_two.info()