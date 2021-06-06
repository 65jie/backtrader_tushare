import backtrader as bt
from backtrader import cerebro
import datas
import strategy

cerebro = bt.Cerebro()
cerebro.adddata(datas.data)
cerebro.addstrategy(strategy.MyStrategy)

startcash = 10000

cerebro.broker.setcash(startcash)
cerebro.broker.setcommission(commission = 0.002)