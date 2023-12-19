import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import *
from preprocess import preprocess

"""
'развитие_опп'
"""


def is_normal(df, col_2):
    if shapiro(df[col_2])[1] >= 0.05:
        c_p = ttest_ind(df['развитие_опп'], df[col_2])

    else:
        c_p = ttest_ind(df['развитие_опп'], df[col_2])
    print(round(c_p[0], 4), round(c_p[1], 4))
    sns.boxplot(data=df, x='развитие_опп', y=col_2)
    plt.show()


def chi_2(df, col_2):
    cross_tab = pd.crosstab(df['развитие_опп'], df[col_2])
    c_p = chi2_contingency(cross_tab)
    print(round(c_p[0], 4), round(c_p[1], 4))
    sns.heatmap(cross_tab, cmap="YlGnBu", annot=True, cbar=False);
    plt.show()


def hypothesis(df: pd.DataFrame) -> None:
    hypo_1(df)
    hypo_2(df)
    hypo_3(df)
    hypo_4(df)
    hypo_5(df)
    hypo_6(df)
    hypo_7(df)
    hypo_8(df)
    hypo_9(df)
    hypo_10(df)


def hypo_1(df) -> None:  # 'хбп' хи квадрат
    chi_2(df, 'хбп')


def hypo_2(df) -> None:  # 'возраст' статы маняуитни
    is_normal(df, "возраст")
    print(pointbiserialr(df['развитие_опп'], df["возраст"]))


def hypo_3(df) -> None:  # 'пол'
    chi_2(df, 'пол')


def hypo_4(df) -> None:  # 'мочевина' маняуитни
    is_normal(df, 'мочевина')
    print(pointbiserialr(df['развитие_опп'], df["мочевина"]))


def hypo_5(df) -> None:  # 'лейкоциты_крови' маняуитни
    is_normal(df, 'лейкоциты_крови')
    print(pointbiserialr(df['развитие_опп'], df["лейкоциты_крови"]))


def hypo_6(df) -> None:  # 'тромбоциты'маняуитни
    is_normal(df, "тромбоциты")
    print(pointbiserialr(df['развитие_опп'], df["тромбоциты"]))


def hypo_7(df) -> None:  # 'общий_белок'маняуитни
    is_normal(df, "общий_белок")
    print(pointbiserialr(df['развитие_опп'], df["общий_белок"]))


def hypo_8(df) -> None:  # 'аик'
    chi_2(df, 'аик')


def hypo_9(df) -> None:  # 'объем_гемотрансфузии'маняуитни
    is_normal(df, "объем_гемотрансфузии")
    print(pointbiserialr(df['развитие_опп'], df["объем_гемотрансфузии"]))


def hypo_10(df):  # 'диурез'маняуитни
    is_normal(df, "диурез")
    print(pointbiserialr(df['развитие_опп'], df["диурез"]))


if __name__ == "__main__":
    data = preprocess("medics_1.csv")
    hypothesis(data)
