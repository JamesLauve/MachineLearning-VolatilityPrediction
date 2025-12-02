import dataLoader.py as dl  
import numpy as np

sp500 = dl.load_stock_data()

#let's print missing values
print(sp500.isnull().sum())

# Basic data cleaning: Fill missing values with forward fill method
sp500.fillna(method='ffill', inplace=True)

sp500['Return'] = sp500['Close'].pct_change()
sp500['LogReturn'] = np.log(sp500['Close'] / sp500['Close'].shift(1))


