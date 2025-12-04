import pandas as pd
import numpy as np
#Here we add a new time features: Day of the Week, month of the year
#However, the model will not be able to understand that 4 and 0 are consecutive days 
#Thus, we will encode those cyclical time features as a Cosine and Sine transformation in the modeling stage

def add_cyclical_time_features(df: pd.DataFrame, date_column: str = 'Date') -> pd.DataFrame:
    """
    Adds cyclical sine and cosine transformations for day of the week and month of the year
    to the DataFrame.
    Args:
        df (pd.DataFrame): The input DataFrame which must contain a datetime column.
        date_column (str): The name of the datetime column in the DataFrame.

    """
    if not pd.api.types.is_datetime64_any_dtype(df[date_column]):
        df[date_column] = pd.to_datetime(df[date_column])

    # Day of Week (0=Monday, 4=Friday) we only consider trading days
    df['day_of_week'] = df[date_column].dt.dayofweek
    df['day_of_week_sin'] = np.sin(2 * np.pi * df['day_of_week'] / 5)
    df['day_of_week_cos'] = np.cos(2 * np.pi * df['day_of_week'] / 5)

    # Month of Year (1=January, 12=December)
    df['month_of_year'] = df[date_column].dt.month
    df['month_of_year_sin'] = np.sin(2 * np.pi * df['month_of_year'] / 12)
    df['month_of_year_cos'] = np.cos(2 * np.pi * df['month_of_year'] / 12)

    
    df = df.drop(columns=['day_of_week', 'month_of_year'])

    return df
