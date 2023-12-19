import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from preprocess import preprocess
from scipy.stats import *


# Пункт 3
def analysis(df: pd.DataFrame) -> None:
    #chronic_diseases(df)
    #imt(df)
    # check_diagnosis(df)
    # dependence_time_fact(df)
    # check_correlations(df)
    dependence_time_fact(df)
    imt_hol(df)
    poch_paren(df)


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
    chronic_kidney_disease_true = round(((df.loc[df['хбп_бин'] == 1, 'развитие_опп']
                                          .sum()) / (sum(df["развитие_опп"]))) * 100, 4)
    chronic_kidney_disease_false = round(((df.loc[df['развитие_опп'] == 0, 'хбп_бин']
                                           .sum()) / (len(df['развитие_опп']) - sum(df["развитие_опп"]))) * 100, 4)

    print(str(diabetes_mellitus_true) + "%", str(diabetes_mellitus_false) + "%")
    print(str(hypertension_true) + "%", str(hypertension_false) + "%")
    print(str(chronic_kidney_disease_true) + "%", str(chronic_kidney_disease_false) + "%")
    # pd.set_option('display.max_rows', None)
    # print(df["хбп_бин"].to_string(index=False))
    # print(len(df["хбп"]))


def draw_chart(labels, sizes, name):
    colors = ['#506D2F', '#2a2922', '#f3ebdd', '#7d5642', "#626D71", "#cdcdc0", "#DDBC95"]
    # Plot
    fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

    wedges, texts = ax.pie(sizes, startangle=-40, colors=colors)

    # Inner circle
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Add labels
    ax.legend(wedges, labels,
              title="болезни",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(texts, size=12, weight="bold")
    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%')
    ax.set_title(name)

    plt.show()


def imt(df):
    # Подпункт 2
    df["имт_ном"] = df["имт"].apply(lambda x: "выраженный_дефицит_массы_тела" if x < 16
    else "недостаточная_масса_тела" if 16 <= x < 18.5
    else "норма" if 18.5 <= x < 25
    else "избыточная_масса_тела" if 25 <= x < 30
    else "ожирение_1_степени" if 30 <= x < 35
    else "ожирение_2_степени" if 35 <= x < 40
    else "ожирение_3_степени")
    # Показатели, которых хоть как-то связаны с сердцем:
    s = '''
    1. ГБ, сахарный диабет
    2. Стенокардия
    3. Инфаркт миокарда, Желудочковая экстрасистолия, Мерцательная аритмия, ХСН, НК
    Разброс: [20, 42]
    Сердце -- почки
    '''
    labels = ["ГБ", "Стенокардия", "Инфаркт миокарда", "Желудочковая экстрасистолия", "Мерцательная аритмия",
              "ХСН", "НК"]
    sizes_norma = count_disease(df, "норма")
    sizes_overweight = count_disease(df, "избыточная_масса_тела")
    sizes_one = count_disease(df, "ожирение_1_степени")
    sizes_two = count_disease(df, "ожирение_2_степени")
    sizes_three = count_disease(df, "ожирение_3_степени")

    draw_chart(labels, sizes_norma, "норма")
    draw_chart(labels, sizes_overweight, "избыточная_масса_тела")
    draw_chart(labels, sizes_one, "ожирение_1_степени")
    draw_chart(labels, sizes_two, "ожирение_2_степени")
    draw_chart(labels, sizes_three, "ожирение_3_степени")
    # print(min(df["имт"]), max(df["имт"]))
    # print(sum(df["развитие_опп"] == 1))
    # sns.scatterplot(data=df, x="имт_ном", y="возраст")
    # plt.show()


def count_disease(df: pd.DataFrame, imt: str) -> list:
    lst = ["гб", "стенокардия", "инфаркт_миокарда", "желудочковая_экстрасистолия",
           "мерцательная_аритмия", "хсн", "нк"]
    answer = []
    for i in range(len(lst)):
        answer.append(df.loc[(df['имт_ном'] == imt) & (df[lst[i]] == 1), 'развитие_опп'].sum())
    return answer


def dependence_time_fact(df: pd.DataFrame) -> None:
    print(pointbiserialr(df["инфаркт_миокарда"], df["длительность_операции"]))
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
    print(chi2_contingency(pd.crosstab(df['ктг_имт'], df['ктг_холестерин'])))
    sns.heatmap(imt_hol, cmap="YlGnBu", annot=True, cbar=False);
    plt.show()
    # нет


def poch_paren(df: pd.DataFrame) -> None:
    poch_paren = df[df["хбп"] == 0]
    print(pearsonr(poch_paren["толщина_паренхимы_почек"], poch_paren["возраст"]))
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


def is_categorical(df: pd.DataFrame, column: str) -> bool:
    return len(df[column].unique()) < len(df) * 0.05


def check_correlations(df: pd.DataFrame) -> list:
    columns = ["возраст", "сахарный_диабет", "гб", "хбп", "сад", "дад", "чсс", "рн", "фракция_изгнания", "холестерин",
               "креатинин_крови", "мочевина", "скф_расч.", "калий", "имт", "толщина_паренхимы_почек"]
    res = []
    for x in columns:
        if is_categorical(df, x):
            temp = chi2_contingency(pd.crosstab(df[x], df["развитие_опп"]))
            res.append([x, "развитие_опп", round(temp[0], 2), round(temp[1], 4), "Хи-квадрат"])
        else:
            if shapiro(df[x])[1] > 0.05:
                temp = ttest_ind(df[x], df["развитие_опп"])
                res.append([x, "развитие_опп", round(temp[0], 2), round(temp[1], 4), "T-критерий Стьюента"])
            else:
                temp = mannwhitneyu(df[x], df["развитие_опп"])
                res.append([x, "развитие_опп", round(temp[0], 2), round(temp[1], 4), "U-критерий Манна-Уитни"])
    print(*res, sep="\n")
    return res


if __name__ == "__main__":
    data = preprocess("medics_1.csv")
    analysis(data)
