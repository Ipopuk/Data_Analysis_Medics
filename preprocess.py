import pandas as pd


def fix_types(df):
    df["развитие_опп"] = df["развитие_опп"].apply(lambda x: 0 if x == "нет" else 1)
    df["хбп"] = df["хбп"].apply(lambda x: 0 if x == "Пациенты без ХБП" else 1 if x == "Стадия C1-C2" else 2)


def preprocess(df_name: str):
    df = pd.read_csv(df_name)
    df.columns = [x.lower().replace(" ", "_") for x in df.columns]
    fix_types(df)


if __name__ == "__main__":
    preprocess("medics_1.csv")
