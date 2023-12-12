import pandas as pd


def add_column(df: pd.DataFrame) -> None:
    df["аик+переливание_крови"] = df["аик"] * (df["объем_гемотрансфузии"].apply(lambda x: 1 if x > 0 else 0))


def check_duplicates(df: pd.DataFrame) -> None:
    df.drop_duplicates(inplace=True)


def drop_nan(df: pd.DataFrame) -> None:
    df.dropna(inplace=True)


def fix_types(df):
    df["развитие_опп"] = df["развитие_опп"].apply(lambda x: 0 if x == "нет" else 1)
    df["хбп"] = df["хбп"].apply(lambda x: 0 if x == "Пациенты без ХБП" else 1 if x == "Стадия C1-C2" else 2)
    for column in df.select_dtypes(include=["object"]).columns:
        df[column] = df[column].apply(lambda x: float(x.replace(",", ".").replace("o", "0")) if type(x) != float else x)


# Пункт 2
def preprocess(df_name: str) -> pd.DataFrame:
    df = pd.read_csv(df_name)
    df.columns = [x.lower().replace(" ", "_").replace(",", "") for x in df.columns]
    fix_types(df)
    drop_nan(df)
    check_duplicates(df)
    add_column(df)
    return df


if __name__ == "__main__":
    preprocess("medics_1.csv")
