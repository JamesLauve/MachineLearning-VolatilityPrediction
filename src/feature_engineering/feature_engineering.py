import numpy as np
import pandas as pd
import yfinance as yf

def add_lagged_features(df: pd.DataFrame, lags: int = 5) -> pd.DataFrame:
    """
    Adds lagged features for the 'log_return' column to the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame containing the 'log_return' column.
        lags (int): The number of lagged features to create.

    Returns:
        pd.DataFrame: The DataFrame with added lagged features.
    """
    for lag in range(1, lags + 1):
        df[f'log_return_lag_{lag}'] = df['log_return'].shift(lag)
    
    for lag in range(1, lags + 1):
        df[f'vol_1day_realized_lag_{lag}'] = df['vol_1day_realized'].shift(lag)
    
    df.dropna(inplace=True)
    
    return df

def add_stock_(df: pd.DataFrame) -> pd.DataFrame:
    df['Nvidia'] = yf.download('NVDA', start='2000-01-01', end='2023-01-01')['Close']

    df.dropna(inplace=True)
    
    return df

def add_cac40(df: pd.DataFrame) -> pd.DataFrame:
    df['CAC40'] = yf.download('^FCHI', start='2000-01-01', end='2023-01-01')['Close']

    df.dropna(inplace=True)
    
    return df

def add_vix(df: pd.DataFrame) -> pd.DataFrame:
    df['VIX'] = yf.download('^VIX', start='2000-01-01', end='2023-01-01')['Close']

    df.dropna(inplace=True)
    
    return df

def add_treasury_yield(df: pd.DataFrame) -> pd.DataFrame:
    df['10Y_Treasury_Yield'] = yf.download('^TNX', start='2000-01-01', end='2023-01-01')['Close']

    df.dropna(inplace=True)
    
    return df

def add_gold_prices(df: pd.DataFrame) -> pd.DataFrame:
    df['Gold_Price'] = yf.download('GC=F', start='2000-01-01', end='2023-01-01')['Close']

    df.dropna(inplace=True)
    
    return df

def add_eur_usd_exchange_rate(df: pd.DataFrame) -> pd.DataFrame:
    df['EUR_USD'] = yf.download('EURUSD=X', start='2000-01-01', end='2023-01-01')['Close']

    df.dropna(inplace=True)
    
    return df





