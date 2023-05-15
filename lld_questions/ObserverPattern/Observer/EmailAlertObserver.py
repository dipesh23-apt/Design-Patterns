from Observer.NotificationAlertObserver import NotificationAlertObserver
from Observable.StockObservable import StockObservable

class EmailAlertObserver(NotificationAlertObserver):
    def __init__(self,email:str,obs:StockObservable):
        self.emailId=email
        self.observable=obs
    def sendmail(self,msg):
        print("Mail sent to",self.emailId)
        print("Message: ",msg)
    def update(self):
        self.sendmail("Product is in stock")