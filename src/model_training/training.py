from sklearn.model_selection import train_test_split
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import LogisticRegression
import numpy as np


def form_prob(df):

    feature_col = ['Return', 'LogReturn', 
                #The lagged features
                'log_return_lag_1', 'log_return_lag_2', 'log_return_lag_3','log_return_lag_4', 'log_return_lag_5',
                'vol_1day_realized_lag_1', 'vol_1day_realized_lag_2', 'vol_1day_realized_lag_3', 'vol_1day_realized_lag_4', 'vol_1day_realized_lag_5',
                #External Features that might correlate
                'Nvidia', 'CAC40', 'VIX', '10Y_Treasury_Yield', 'Gold_Price', 'EUR_USD',
                #momentum features
                'log_return_ma_5', 'rsi',
                #Cyclical time features
                'day_of_week_sin', 'day_of_week_cos', 'month_of_year_sin', 'month_of_year_cos',
                ]
    target_col = 'Target_Vol'
    #We might want to predict the log volatility instead because it is positive and might be more normally distributed
    # We will check which 
    # target_col = 'log_vol_target'

    X = df[feature_col]
    y = df[target_col]
    print("Feature matrix shape:", X.shape)
    print("Target vector shape:", y.shape)
    return X, y

def rolling_split_data(X, y, test_size=0.2, splits=5, model= LogisticRegression ):
    tss = TimeSeriesSplit(n_splits=splits, test_size=int(len(X)*test_size))
    for fold, (train_index, test_index) in enumerate(tss.split(X)):
        print(f"Fold {fold}")
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        yield X, y_test, y_pred