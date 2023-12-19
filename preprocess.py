import numpy as np
import pandas as pd


def add_column(df: pd.DataFrame) -> None:
    df["аик+переливание_крови"] = df["аик"] * (df["объем_гемотрансфузии"].apply(lambda x: 1 if x > 0 else 0))


def check_duplicates(df: pd.DataFrame) -> None:
    df.drop_duplicates(inplace=True)


def drop_nan(df: pd.DataFrame) -> None:
    df.dropna(inplace=True)


def fix_types(df: pd.DataFrame) -> None:
    df["развитие_опп"] = df["развитие_опп"].apply(lambda x: 0 if x == "нет" else 1)
    df["хбп"] = df["хбп"].apply(lambda x: 0 if x == "Пациенты без ХБП" else 1 if x == "Стадия C1-C2" else 2)
    for column in df.select_dtypes(include=["object"]).columns:
        df[column] = df[column].apply(lambda x: float(x.replace(",", ".").replace("o", "0")) if type(x) != float else x)


def drop_outliers(df: pd.DataFrame, a=3) -> tuple:
    columns = df.columns
    outliers_all = np.array([False for i in range(len(df))])
    for column in columns:
        if len(df[column].unique()) > len(df) * 0.05:
            std = df[column].std()
            median = df[column].median()
            outliers = abs(df[[column]] - median) > a * std
            outliers_all = np.bitwise_or(outliers.to_numpy().flatten(), outliers_all)
    df_unchanged = df.copy()
    df = df[~ outliers_all].dropna()
    return df, df_unchanged, outliers_all


# Пункт 2
def preprocess(df_name: str) -> pd.DataFrame:
    df = pd.read_csv(df_name)
    df.columns = [x.lower().replace(" ", "_").replace(",", "") for x in df.columns]
    df.columns = [x[:-1] if x[-1] == "_" else x for x in df.columns]
    fix_types(df)
    drop_nan(df)
    check_duplicates(df)
    df, unchanged_df, outliers = drop_outliers(df)
    add_column(df)
    return df


if __name__ == "__main__":
    preprocess("medics_1.csv")
