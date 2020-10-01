import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl

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

  return adj_close, moving_avg, input

def plot_rolling_average(close_px, mavg, input):
  mpl.rc('figure', figsize=(8, 7))
  mpl.__version__
  style.use('ggplot')
  close_px.plot(label='AAPL')
  mavg.plot(label='mavg')
  plt.legend()
  plt.show()
