import datas
import cerebro

d1 = datas.start.strftime('%Y%m%d')
d2 = datas.end.strftime('%Y%m%d')
print(f'初始资金： {cerebro.startcash}\n回测期间:{d1}:{d2}')

cerebro.cerebro.run()

portvalue = cerebro.cerebro.broker.getvalue()
pnl = portvalue - cerebro.startcash

print(f'总资金：{round(portvalue, 2)}')
print(f'净收益： {round(pnl, 2)}')
