from preprocess import preprocess


# Пункт 3
def analysis(df):
    dependence_time_fact(df)


def dependence_time_fact(df):
    # Подпункт 1
    diabetes_mellitus_true = round(((sum(df.loc[:, "сахарный_диабет"]) / sum(df["развитие_опп"])) * 100), 4)
    diabetes_mellitus_false = round(((sum(df.loc[:, "сахарный_диабет"]) / (len(df) - sum(df["развитие_опп"]))) * 100),
                                    4)
    hypertension_true = ""
    hypertension_false = ""
    chronic_kidney_disease_true = ""
    chronic_kidney_disease_false = ""

    # print(str(diabetes_mellitus_true) + "%", str(diabetes_mellitus_false) + "%")
    # print(str(hypertension_true) + "%", str(hypertension_false) + "%")
    # print(str(chronic_kidney_disease_true + "%"), str(chronic_kidney_disease_false) + "%")

    # Подпункт 3
    print(df[["инфаркт_миокарда", "длительность_операции"]].corr())


if __name__ == "__main__":
    data = preprocess("medics_1.csv")
    analysis(data)
