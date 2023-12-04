from preprocess import preprocess


# Пункт 3
def analysis(df):
    dependence_time_fact(df)


def dependence_time_fact(df):
    # Подпункт 3
    print(df[["инфаркт_миокарда", "длительность_операции"]].corr())


if __name__ == "__main__":
    data = preprocess("medics_1.csv")
    analysis(data)
