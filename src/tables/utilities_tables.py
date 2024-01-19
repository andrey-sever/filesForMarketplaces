import pandas as pd
from src.tables.PatternTable import PatternTable


def merge_tables(tables: list[pd.DataFrame]):
    """
    Соединение таблиц из входящего списка в
    одну таблицу. Таблицы DataFrame
    :return таблица типа DataFrame
    """
    new_table = pd.DataFrame()
    for table in tables:
        if new_table.empty:
            new_table = table
            continue
        new_table = pd.concat([new_table, table], sort=False, axis=0, ignore_index=True)
    return new_table

def add_balance_price(data_in: PatternTable, general_price_list: pd.DataFrame):
    """
    Добавление в файл остатка и цены. Можно по отдельности.
    :param data_in: объект шаблона
    :param general_price_list: общий прайс лист в формате DataFrame
    :return: сохраняет файл в папку data_out
    """
    df_in = data_in.get_table()
    name_quantity = data_in.get_matching()['Остаток']
    name_price = data_in.get_matching()['Цена']
    # Если колонка существует
    fill_quantity = {name_quantity}.issubset(df_in.columns)
    fill_price = {name_price}.issubset(df_in.columns)

    for index, row in df_in.iterrows():
        found_string = general_price_list.loc[general_price_list['Артикул'] == row['Артикул']]
        if found_string.empty:
            continue

        if fill_quantity:
            df_in.at[index, name_quantity] = found_string['Остаток']
        if fill_price:
            df_in.at[index, name_price] = found_string['Цена']

    path_out = f'data_out/{data_in.get_name_out()}.xlsx'
    df_in.to_excel(path_out, index=False)