import numpy as np
import pandas as pd
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

"""
Столбцы для предсказания:
'возраст', 'пол', 'гб', 'сахарный_диабет',
'стенокардия', 'инфаркт_миокарда', 'мерцательная_аритмия',
'желудочковая_экстрасистолия', 'а-в_блокада',
'блокада_ножек_пучка_гиса', 'сад', 'дад', 'креатинин_крови',
'мочевина_', 'калий', 'натрий', 'хлориды', 'кальций', 'рн',
'ве', 'нсо3', 'ро2', 'рсо2', 'оксигем.', 'общ.со2', 'гемоглобин',
'лейкоциты_крови', 'тромбоциты', 'холестерин',
'триглицериды', 'лпонп', 'лпнп', 'общий_белок', 'имт'
"""

"""
Модель предсказывает:
'скф_расч.'
"""


def fit_model(X: np.array, y: np.array) -> CatBoostRegressor:
    regressor = CatBoostRegressor(n_estimators=10000, max_depth=3, learning_rate=0.01)
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)
    regressor.fit(X_train, y_train, eval_set=(X_test, y_test), use_best_model=True)
    print(f"RMSE при  определении СКФ: {mean_squared_error(regressor.predict(X_test), y_test) ** 0.5}")
    regressor.save_model("regressor.cbm")
    print("Модель сохранена как regressor.cbm")
    return regressor


def predict(X: np.array, model="regressor.cbm") -> float:
    regressor = CatBoostRegressor()
    regressor.load_model(model)
    return regressor.predict(X)
