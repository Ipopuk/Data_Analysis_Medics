import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from preprocess import preprocess


# Пункт 3
def analysis(df: pd.DataFrame) -> None:
    check_diagnosis(df)
    #dependence_time_fact(df)
    #imt_hol(df)
    #poch_paren(df)


def chronic_diseases(df: pd.DataFrame) -> None:
    # Подпункт 1
    diabetes_mellitus_true = round(((df.loc[df['развитие_опп'] == 1, 'сахарный_диабет']
                                     .sum()) / (sum(df["развитие_опп"]))) * 100, 4)
    diabetes_mellitus_false = round(((df.loc[df['развитие_опп'] == 0, 'сахарный_диабет']
                                      .sum()) / (len(df['развитие_опп']) - sum(df["развитие_опп"]))) * 100, 4)

    hypertension_true = round(((df.loc[df['развитие_опп'] == 1, 'гб']
                                .sum()) / (sum(df["развитие_опп"]))) * 100, 4)
    hypertension_false = round(((df.loc[df['развитие_опп'] == 0, 'гб']
                                 .sum()) / (len(df['развитие_опп']) - sum(df["развитие_опп"]))) * 100, 4)

    df["хбп_бин"] = df["хбп"].apply(lambda x: 1 if x == 1 or x == 2 else 0)
    # chronic_kidney_disease_true = round(((df.loc[df['развитие_опп'] == 1, 'хбп_бин']
    #                                       .sum()) / (sum(df["развитие_опп"]))) * 100, 4)
    # chronic_kidney_disease_false = round(((df.loc[df['развитие_опп'] == 0, 'хбп_бин']
    #                                        .sum()) / (len(df['развитие_опп']) - sum(df["развитие_опп"]))) * 100, 4)

    print(str(diabetes_mellitus_true) + "%", str(diabetes_mellitus_false) + "%")
    print(str(hypertension_true) + "%", str(hypertension_false) + "%")
    # wrong
    # print(str(chronic_kidney_disease_true) + "%", str(chronic_kidney_disease_false) + "%")
    # print((df.loc[df['развитие_опп'] == 1, 'хбп_бин'].sum()))

    pd.set_option('display.max_rows', None)
    # print(df["хбп_бин"].to_string(index=False))
    # Подпункт 2
    df["имт_ном"] = df["имт"].apply(lambda x: "выраженный_дефицит_массы_тела" if x < 16
    else "недостаточная_масса_тела" if 16 <= x < 18.5
    else "норма" if 18.5 <= x < 25
    else "избыточная_масса_тела" if 25 <= x < 30
    else "ожирение_1_степени" if 30 <= x < 35
    else "ожирение_2_степени" if 35 <= x < 40
    else "ожирение_3_степени")


def dependence_time_fact(df: pd.DataFrame) -> None:
    print(stats.pointbiserialr(df["инфаркт_миокарда"], df["длительность_операции"]))
    infarct_0 = df[df["инфаркт_миокарда"] == 0]
    infarct_1 = df[df["инфаркт_миокарда"] == 1]
    fig, axes = plt.subplots(1, 2, figsize=(9, 3))
    plot = sns.boxplot(ax=axes[0], data=infarct_0, y="длительность_операции")
    plot2 = sns.boxplot(ax=axes[1], data=infarct_1, y="длительность_операции")
    plt.show()
    # нет


def imt_hol(df: pd.DataFrame) -> None:
    # !!! норма - 18,5-25 избыточный - 25-30, больше - ожирение
    # норма 3,6-7,8 ммоль и моль!!!
    df["ктг_имт"] = df["имт"].apply(lambda x: 1 if x > 25 else 0)
    df["ктг_холестерин"] = df["холестерин"].apply(lambda x: 1 if x > 7.8 else 0)
    imt_hol = pd.crosstab(df['ктг_имт'], df['ктг_холестерин'])
    print(imt_hol)
    print(stats.chi2_contingency(pd.crosstab(df['ктг_имт'], df['ктг_холестерин'])))
    sns.heatmap(imt_hol, cmap="YlGnBu", annot=True, cbar=False);
    plt.show()
    # нет


def poch_paren(df: pd.DataFrame) -> None:
    poch_paren = df[df["хбп"] == 0]
    print(stats.pearsonr(poch_paren["толщина_паренхимы_почек"], poch_paren["возраст"]))
    sns.scatterplot(data=poch_paren, x="толщина_паренхимы_почек", y="возраст")
    plt.show()
    # нет


def get_diagnosis(m: int) -> str:
    if m > 100:
        return "Пациенты без ХБП"
    if m > 60:
        return "Стадия C1-C2"
    return "Стадия С3"


def check_diagnosis(df: pd.DataFrame) -> list:  # ?
    num_to_words = {0: "Пациенты без ХБП", 1: "Стадия C1-C2", 2: "Стадия С3"}
    wrong_diagnosis = []
    for idx, row in df.iterrows():
        if row["скф_расч."] > 100:
            if row["хбп"] != 0:
                print(
                    f"У пациента {idx} диагноз {num_to_words[row['хбп']]}, но должен быть {get_diagnosis(row['скф_расч.'])}")
                wrong_diagnosis.append(idx)
        elif row["скф_расч."] > 60:
            if row["хбп"] != 1:
                print(
                    f"У пациента {idx} диагноз {num_to_words[row['хбп']]}, но должен быть {get_diagnosis(row['скф_расч.'])}")
                wrong_diagnosis.append(idx)
        elif row["скф_расч."] != 2:
            print(
                f"У пациента {idx} диагноз {num_to_words[row['хбп']]}, но должен быть {get_diagnosis(row['скф_расч.'])}")
            wrong_diagnosis.append(idx)
    return wrong_diagnosis


if __name__ == "__main__":
    data = preprocess("medics_1.csv")
    analysis(data)
