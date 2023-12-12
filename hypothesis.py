import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import *
from preprocess import preprocess

"""
'развитие_опп'
"""
def isnormal(col_2):
    if shapiro(col_2)[1] >= 0.05:
        #ttest
        pass
    else:
        mannwhitneyu(col_2)


def hypothesis(df: pd.DataFrame) -> None:
       pass


def hypo_1(): # 'хбп' хи квадрат
    pass


def hypo_2(): # 'возраст' статы маняуитни
    pass


def hypo_3(): # 'пол' pointbiserialr
    pass


def hypo_4(): #'мочевина' маняуитни
    pass


def hypo_5(): #'лейкоциты_крови' маняуитни
    pass


def hypo_6(): #'тромбоциты'маняуитни
    pass


def hypo_7(): #'общий_белок'маняуитни
    pass


def hypo_8(): #'аик'  pointbiserialr
    pass


def hypo_9(): #'объем_гемотрансфузии'маняуитни
    pass


def hypo_10(): #'диурез'маняуитни
    pass


if __name__ == "__main__":
    data = preprocess("medics_1.csv")
    hypothesis(data)
