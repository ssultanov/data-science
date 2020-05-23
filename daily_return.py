import pandas as pd
from pandas_datareader import data as wb
from sys import argv

def simple_return(start, ticker, *args):
    stock_data = wb.DataReader(ticker, data_source='yahoo', start=start)
    data = (stock_data['Adj Close'] / stock_data['Adj Close'].shift(1)) - 1
    file_name = 'daily_return_' + str(ticker) + '.csv'
    data.to_csv(file_name)

simple_return(*argv[1:])

hello = 'Hello from GitHub'
