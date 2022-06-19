import pandas as pd


def ffill(df, columns_list, id='cusip'):
    """
    Function to fill in missing values in a forward manner.

    :param df: dataframe to be transformed
    :type df: pandas.dataframe
    :param columns_list: list of columns to fill forward
    :type columns_list: list
    :param id: identity used to create groups
    :type id: str
    :return: df (forward filled)
    """
    df_ffill = df.copy()

    for column in columns_list:
        df_ffill[column] = (df_ffill.groupby(id)[column].ffill())

    return df_ffill


def mfill(df, columns_list, date='datadate'):
    """
    Function to fill in missing values by taking median of cross-section.

    :param df: dataframe to be transformed
    :type df: pandas.dataframe
    :param columns_list: list of columns to fill median for
    :type columns_list: list
    :param date: column with time index
    :type date: str
    :return: df (median filled)
    """
    df_mfill = df.copy()

    for column in columns_list:
        df_mfill[column] = df_mfill[column].fillna(df_mfill.groupby(date)[column].transform('median'))

    return df_mfill


def lagged(df, columns_list, id='cusip', date='datadate', lags_list=[-5,-4,-3,-2,-1,1]):
    """
    Function to add lags in the dataframe.
    
    :param df: dataframe to be transformed
    :type df: pandas.dataframe
    :param columns_list: list of columns for which to create lags
    :type columns_list: list
    :param id: identity used to create groups
    :type id: str
    :param date: column with time index
    :type data: str
    :return: df (forward filled)
    :param lags_list: amount of lags required
    :type lags_list: list
    :return: df (with new lag columns)
    """
    lags_list = [-i for i in lags_list]
    df_lagged = df.copy().sort_values(by=date)  
    X_col_list = columns_list.copy()
    y_col_list = []

    for lag in lags_list:
        for column in columns_list:
            new_col_name = column + str('_') + str(-lag)
            df_lagged[new_col_name] = (df_lagged.groupby(id)[column].shift(lag))

            if(lag < 0):
                y_col_list.append(new_col_name)
            else:
                X_col_list.append(new_col_name)

    return df_lagged, X_col_list, y_col_list


def ttm(df, columns_list=['revtq', 'cogsq', 'xsgaq', 'niq', 'ebitq'], id='cusip', date='datadate'):
    """
    Function to convert quarterly data into trailing twelve months (TTM) data.
    
    :param df: dataframe to be transformed
    :type df: pandas.dataframe
    :param columns_list: list of columns to transform to TTM format
    :type columns_list: list
    :param id: identity used to create groups
    :type id: str
    :param date: column with time index
    :type data: str
    :return: df (with new TTM format)
    """
    df_ttm = df.copy()
    df_ttm_shuffled = df.copy()
    columns_list_drop = columns_list.copy()
    columns_list.append(date)
    columns_list.append(id)

    df_ttm = df_ttm.drop(columns_list_drop, axis=1)
    df_ttm_shuffled = df_ttm_shuffled.groupby(id)[columns_list].rolling('365D', on=date, min_periods=4).sum().reset_index()[columns_list]
    df_ttm = pd.merge(df_ttm, df_ttm_shuffled, how='inner', on=[id, date])

    return df_ttm