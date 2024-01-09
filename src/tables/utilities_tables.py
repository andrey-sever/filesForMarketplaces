import pandas as pd


def merge_tables(tables: list[pd.DataFrame]):
    """
    Соединение таблиц из входящеко списка в
    одну таблицу. Таблицы DataFrame
    """
    new_table = pd.DataFrame()
    for table in tables:
        if new_table.empty:
            new_table = table
            continue
        new_table = pd.concat([new_table, table], sort=False, axis=0, ignore_index=True)
    return new_table
