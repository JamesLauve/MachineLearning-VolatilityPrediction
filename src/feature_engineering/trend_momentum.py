import pandas as pd
import yfinance as yf
import numpy as np


# We add a moving average feature for the 'log_return' column 
def moving_average(df: pd.DataFrame, window: int = 5) -> pd.DataFrame:
    """
    Args:
        df (pd.DataFrame): The input DataFrame containing the 'log_return' column.
        window (int): The window size for the moving average.
    """
    df[f'log_return_ma_{window}'] = df['log_return'].rolling(window=window).mean()
    
    df.dropna(inplace=True)
    
    return df

# We add a Relative Strength Index (RSI) feature
def relative_strength_index(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
  
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    df['rsi'] = 100 - (100 / (1 + rs))
    
    df.dropna(inplace=True)
    
    return df