import pandas as pd
import numpy as np


time_format = '%H:%M:%S'


def check_owl_or_lark(df: pd.DataFrame) -> pd.DataFrame:
    owl_or_lark = []
    for index, row in df.iterrows():
        if pd.to_datetime(row['Время засыпания'], format=time_format) >= \
                pd.to_datetime('23:00:00', format=time_format) \
                or pd.to_datetime(row['Время засыпания'], format=time_format) < \
                pd.to_datetime('5:00:00', format=time_format):

            if pd.to_datetime(row['Время пробуждения'], format=time_format) >= \
                    pd.to_datetime('10:00:00', format=time_format):
                owl_or_lark.append('owl')
            else:
                owl_or_lark.append('pigeon')
        else:
            if pd.to_datetime(row['Время пробуждения'], format=time_format) < \
                    pd.to_datetime('10:00:00', format=time_format):
                owl_or_lark.append('lark')
            else:
                owl_or_lark.append('pigeon')

    df.insert(25, 'Сова/Жаворонок/Голубь', owl_or_lark, True)
    df['Сова/Жаворонок/Голубь'] = df['Сова/Жаворонок/Голубь'].astype('category')
    return df


def check_amount_of_sleep(df: pd.DataFrame) -> pd.DataFrame:
    amount_of_sleep = []
    for index, row in df.iterrows():
        time = pd.to_datetime(row['Время пробуждения'], format=time_format) - pd.to_datetime(row['Время засыпания'],
                                                                                             format=time_format)
        amount_of_sleep.append(int(time.to_pytimedelta().seconds / 3600))

    df.insert(26, 'Часов сна', amount_of_sleep, True)
    df['Часов сна'] = df['Часов сна'].astype(np.int8)
    return df


def remove_unnecessary_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=['Время засыпания', 'Время пробуждения'], axis=1)
    return df


def feature_generation(df: pd.DataFrame) -> pd.DataFrame:
    df = check_owl_or_lark(df)
    df = check_amount_of_sleep(df)
    df = remove_unnecessary_columns(df)
    # df = cast_types(df)
    return df
