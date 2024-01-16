import pandas as pd


def merge_tables(tables: list[pd.DataFrame]):
    """
    Соединение таблиц из входящего списка в
    одну таблицу. Таблицы DataFrame
    """
    new_table = pd.DataFrame()
    for table in tables:
        if new_table.empty:
            new_table = table
            continue
        new_table = pd.concat([new_table, table], sort=False, axis=0, ignore_index=True)
    return new_table

def add_balance_price(path_file_in: str, general_price_list: pd.DataFrame):
    """
    Добавление в файл остатка и цены. Можно по отдельности.
    :param path_file_in: путь к файлу, куда добавлять
    :param general_price_list: общий прайс лист в формате DataFrame
    :return: сохраняет файл по тому же пути
    """
    df_in = pd.read_excel(path_file_in)
    for index, row in df_in.iterrows():
        found_string = general_price_list.loc[general_price_list['Артикул'] == row['Артикул']]
        df_in.at[index, 'Остаток'] = found_string['Остаток']
        df_in.at[index, 'Цена'] = found_string['Цена']
    df_in.to_excel('data_in/Озон_цены_остатки.xlsx', index=False)