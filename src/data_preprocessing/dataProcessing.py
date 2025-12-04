import dataLoader.py as dl  
import numpy as np
import matplotlib.pyplot as plt

sp500 = dl.load_stock_data()
def SetReturns(data):
    
    #let's print missing values
    print(data.isnull().sum())

    # Basic data cleaning: Fill missing values with forward fill method
    data.fillna(method='ffill', inplace=True)

    data['Return'] = data['Close'].pct_change()
    data['LogReturn'] = np.log(data['Close'] / data['Close'].shift(1))

    #Let's observe our data information after processing
    print('Statistical Summary after Processing:')
    print(sp500.describe())

def plotting_SP(data):
    plt.figure(figsize=(12, 5))
    plt.plot(data.index, data["Close"])
    plt.title("S&P 500 - Close")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()

def plotting_Histo_Returns(data):
    plt.figure(figsize=(10, 4))
    plt.hist(data["Returns"].dropna(), bins=100)
    plt.title("Histogram of Daily Log Returns")
    plt.xlabel("Returns")
    plt.ylabel("Frequency")
    plt.show()



