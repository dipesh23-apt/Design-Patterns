from Observer.NotificationAlertObserver import NotificationAlertObserver
from Observable.StockObservable import StockObservable

class MobileAlertObserver(NotificationAlertObserver):
    def __init__(self,phone:str,obs:StockObservable):
        self.phone=phone
        self.observable=obs
    def sendmsg(self,msg):
        print("Msg sent to",self.phone)
        print("Message: ",msg)
    def update(self):
        self.sendmsg("Product is in stock...Hurry Up !!")