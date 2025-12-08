import sys
import os

#Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(file), 'src')))

from data_preprocessing import dataLoader as dl

def main():
    print("Welcome to the volatility prediction project!")
    df = dl.load_stock_data()
    print("Data loaded successfully.")


if name == "main":
    main()
