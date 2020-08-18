#Sean Curran
#A simple program to get the opening and closing prices for a given stock,
#the prices are graphed and the data is written into a CSV file.
#User needs to provide their own Alpha Vantage code.
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import datetime

ALPHA_VAN = 'Your alpha vantage code here'

start = str(datetime.datetime.strftime(datetime.datetime.now()- datetime.timedelta((50)), '%Y-%m-%d'))
end = str(datetime.datetime.today().strftime('%Y-%m-%d'))
font = {'family' : 'normal','weight' : 'normal','size' : '8'}

def get_data(ticker_sym):
   style.use('ggplot')
   stock_data = web.DataReader(ticker_sym, 'av-daily', start, end,api_key=ALPHA_VAN)
   stock_data.to_csv(ticker_sym + '.csv')
   ax = stock_data['close'].plot(figsize= (11,8),label = "Close", legend = True)
   ax = stock_data['open'].plot(figsize= (11,8), label = "Open", legend = True)
   ax.set_ylabel("Price : USD")
   ax.set_xlabel("Date")
   plt.rc('font', **font)
   plt.title(ticker_sym)
   plt.show()
   print(stock_data)

get_data('TSLA')

