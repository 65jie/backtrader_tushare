import backtrader as bt

class MyStrategy(bt.Strategy):
    params = (
        ('maperiod', 20),
    )

    def __init__(self) -> None:
        super().__init__()
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None
        self.buycomm = None

        self.sma = bt.indicators.MovingAverageSimple(
            self.datas[0], period = self.params.maperiod
        )

    def next(self):
        if self.order:
            return
        
        if not self.position:
            if self.dataclose[0] > self.sma[0]:
                self.order = self.buy(size = 500)

        else:
            if self.dataclose[0] < self.sma[0]:
                self.order = self.sell(size = 500)