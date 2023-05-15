from Observable.StockObservable import StockObservable
from Observer.NotificationAlertObserver import NotificationAlertObserver

class IphoneObservable(StockObservable):
    def __init__(self):
        self.observerList=[]
        self.stockCount=0
    def add(self,observer:NotificationAlertObserver):
        self.observerList.append(observer)

    def remove(self,observer:NotificationAlertObserver):
        self.observerList.remove(observer)

    def notifySubscriber(self):
        for i in range(len(self.observerList)):
            self.observerList[i].update()

    def setStockCount(self,value):
        self.stockCount+=value
        #print(self.stockCount)
        if self.stockCount!=0:
            self.notifySubscriber()
        

    def getStockCount(self):
        return self.stockCount
