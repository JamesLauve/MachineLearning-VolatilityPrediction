import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split

def load_stock_data():

    sp500 = yf.download('^GSPC', start='2000-01-01', end='2023-01-01')
    print (sp500.head())    
    print (sp500.tail())

