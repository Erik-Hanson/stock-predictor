import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame

def search_company_stock_history():
  name = input("Please enter a company name you wish to search for: ")
  start = datetime.datetime(2010, 1, 1)  # TODO: Make this configurable as well
  end = datetime.datetime(2020, 1, 11)  # TODO: Make this configurable as well

  df = web.DataReader(name, 'yahoo', start, end)
  print(df.tail())

def compute_rolling_average():
  name = input("Please enter a company name you wish to search for: ")
  start = datetime.datetime(2010, 1, 1)  # TODO: Make this configurable as well
  end = datetime.datetime(2020, 1, 11)  # TODO: Make this configurable as well

  df = web.DataReader(name, 'yahoo', start, end)
  adj_close = df['Adj Close']
  moving_avg = adj_close.rolling(100).mean()
  print("Moving Average: " + str(moving_avg.tail()))
