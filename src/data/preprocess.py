import pandas as pd
import numpy as np
from src.config import *


def set_idx(df: pd.DataFrame, idx_col: str) -> pd.DataFrame:
    df = df.set_index(idx_col)
    return df


def drop_unnecessary_id(df: pd.DataFrame) -> pd.DataFrame:
    if 'ID_y' in df.columns:
        df = df.drop('ID_y', axis=1)
    return df


def add_ord_edu(df: pd.DataFrame) -> pd.DataFrame:
    df[f'{EDU_COL}_ord'] = df[EDU_COL].str.slice(0, 1).astype(np.int8).values
    df = df.drop(columns=[EDU_COL])
    return df


def fill_sex(df: pd.DataFrame) -> pd.DataFrame:
    most_freq = df[SEX_COL].value_counts().index[0]
    df[SEX_COL] = df[SEX_COL].fillna(most_freq)
    return df


def cast_types(df: pd.DataFrame) -> pd.DataFrame:
    df[CAT_COLS] = df[CAT_COLS].astype('category')

    ohe_int_cols = df[OHE_COLS].select_dtypes('number').columns
    df[ohe_int_cols] = df[ohe_int_cols].astype(np.int8)

    df[REAL_COLS] = df[REAL_COLS].astype(np.float32)
    return df


def delete_nan_value(df: pd.DataFrame) -> pd.DataFrame:
    # Курение
    period_smoke = list(df['Возраст курения'])
    number_of_cigarettes = list(df['Сигарет в день'])
    count = 0
    for index, row in df.iterrows():
        if row['Статус Курения'] == 'Никогда не курил(а)':
            if pd.isna(row['Возраст курения']):
                period_smoke[count] = 0
            if pd.isna(row['Сигарет в день']):
                number_of_cigarettes[count] = 0
        count += 1
    df = df.drop(columns=['Возраст курения', 'Сигарет в день'])
    count = 0
    for index, row in df.iterrows():
        df.loc[index, 'Возраст курения'] = period_smoke[count]
        df.loc[index, 'Сигарет в день'] = number_of_cigarettes[count]
        count += 1
    df = df[(np.isnan(df['Возраст курения'])) == False]
    df['Возраст курения'] = df['Возраст курения'].astype(np.int8)
    df = df[(np.isnan(df['Сигарет в день'])) == False]
    df['Сигарет в день'] = df['Сигарет в день'].astype(np.int8)

    # Пассивное курение
    frequency_second_hand_smoke = list(df['Частота пасс кур'])
    count = 0
    for index, row in df.iterrows():
        if row['Пассивное курение'] == 0:
            if pd.isna(row['Частота пасс кур']):
                frequency_second_hand_smoke[count] = 'менее 1 раза в день'
        count += 1
    df = df.drop(columns=['Частота пасс кур'])
    df.insert(21, 'Частота пасс кур', frequency_second_hand_smoke, True)
    df = df[(pd.isna(df['Частота пасс кур'])) == False]
    df['Частота пасс кур'] = df['Частота пасс кур'].astype('category')

    # Алкоголь
    drinking_period = list(df['Возраст алког'])
    count = 0
    for index, row in df.iterrows():
        if row['Алкоголь'] == 'никогда не употреблял':
            if pd.isna(row['Возраст алког']):
                drinking_period[count] = 0
        count += 1
    df = df.drop(columns=['Возраст алког'])
    count = 0
    for index, row in df.iterrows():
        df.loc[index, 'Возраст алког'] = drinking_period[count]
        count += 1
    df = df[(pd.isna(df['Возраст алког']) == False)]
    df['Возраст алког'] = df['Возраст алког'].astype(np.int8)
    return df


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = set_idx(df, ID_COL)
    df = drop_unnecessary_id(df)
    df = fill_sex(df)
    df = cast_types(df)
    df = add_ord_edu(df)
    df = delete_nan_value(df)
    return df


def preprocess_target(df: pd.DataFrame) -> pd.DataFrame:
    df[TARGET_COLS] = df[TARGET_COLS].astype(np.int8)
    return df


# def extract_target(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
def extract_target(df: pd.DataFrame):
    df, target = df.drop(TARGET_COLS, axis=1), df[TARGET_COLS]
    return df, target
