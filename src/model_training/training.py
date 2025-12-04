from sklearn.model_selection import train_test_split



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

    X = df[feature_col]
    y = df[target_col]
    print("Feature matrix shape:", X.shape)
    print("Target vector shape:", y.shape)
    return X, y

def split_data(X, y, test_size=0.2):
    split_index = int(len(X) * (1 - test_size))
    X_train, X_test = X[:split_index], X[split_index:]
    y_train, y_test = y[:split_index], y[split_index:]

    print("Train size:", X_train.shape[0])
    print("Test size :", X_test.shape[0])

    return X_train, X_test, y_train, y_test

