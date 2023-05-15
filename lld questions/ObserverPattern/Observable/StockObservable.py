from abc import ABC,abstractmethod
from Observer.NotificationAlertObserver import NotificationAlertObserver

class StockObservable(ABC):
    # def __init__(self):
    #     self.observerList=[]
    #     self.stockCount=0
    @abstractmethod
    def add(self,observer:NotificationAlertObserver):
        pass

    @abstractmethod
    def remove(self,observer:NotificationAlertObserver):
        pass

    @abstractmethod
    def notifySubscriber(self):
        pass
    @abstractmethod
    def setStockCount(self,value):
        pass
    @abstractmethod
    def getStockCount(self):
        pass
