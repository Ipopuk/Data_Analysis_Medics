import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import *
from preprocess import preprocess

"""
'развитие_опп'
"""


def isnormal(df, col_2):
    if shapiro(df[col_2])[1] >= 0.05:
        print(ttest_ind(df['развитие_опп'], df[col_2]))

    else:
        print(mannwhitneyu(df['развитие_опп'], df[col_2]))
    sns.boxplot(data=df, x='развитие_опп', y=col_2)
    plt.show()


def chi_2(df, col_2):
    cross_tab = pd.crosstab(df['развитие_опп'], df[col_2])
    print(chi2_contingency(cross_tab))
    sns.heatmap(cross_tab, cmap="YlGnBu", annot=True, cbar=False);
    plt.show()


def hypothesis(df: pd.DataFrame) -> None:
    hypo_1(df)
    hypo_2(df)
    hypo_3(df)
    hypo_4(df)
    hypo_5(df)


def hypo_1(df) -> None:  # 'хбп' хи квадрат
    chi_2(df, 'хбп')


def hypo_2(df) -> None:  # 'возраст' статы маняуитни
    isnormal(df, "возраст")
    print(pointbiserialr(df['развитие_опп'], df["возраст"]))


def hypo_3(df) -> None:  # 'пол'
    chi_2(df, 'пол')


def hypo_4(df) -> None:  # 'мочевина' маняуитни
    isnormal(df, 'мочевина')
    print(pointbiserialr(df['развитие_опп'], df["мочевина"]))


def hypo_5(df) -> None:  # 'лейкоциты_крови' маняуитни
    isnormal(df, 'лейкоциты_крови')
    print(pointbiserialr(df['развитие_опп'], df["лейкоциты_крови"]))


def hypo_6():  # 'тромбоциты'маняуитни
    pass


def hypo_7():  # 'общий_белок'маняуитни
    pass


def hypo_8():  # 'аик'  pointbiserialr
    pass


def hypo_9():  # 'объем_гемотрансфузии'маняуитни
    pass


def hypo_10():  # 'диурез'маняуитни
    pass


if __name__ == "__main__":
    data = preprocess("medics_1.csv")
    hypothesis(data)
