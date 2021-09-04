from datetime import datetime

import backtrader as bt
import matplotlib.pyplot as plt
import pandas as pd
import tushare as ts
from pylab import mpl

mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.sans-serif'] = ['SimHei']

def getData(code, start = '2010-01-01', end = '2020-03-31'):
    df = ts.get_k_data(code, autype = 'qfq', start = start, end = end)
    df.index = pd.to_datetime(df.date)
    df['openinterest'] = 0
    df = df[['open', 'high', 'low', 'close', 'volume', 'openinterest']]
    return df

dataframe = getData('600000')

start = datetime(2010, 3, 31)
end = datetime(2020, 3, 31)

data = bt.feeds.PandasData(dataname = dataframe, fromdate = start, todate = end)