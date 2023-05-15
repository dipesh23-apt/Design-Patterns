from Observable.IphoneObservable import IphoneObservable
from Observer.EmailAlertObserver import EmailAlertObserver
from Observer.MobileAlertObserver import MobileAlertObserver
class Store:
    def main():
        observable_iphone=IphoneObservable()
        observer1=EmailAlertObserver("xyz1@gmail.com",observable_iphone)
        observer2=MobileAlertObserver("7381xxxxxx",observable_iphone)
        observer3=EmailAlertObserver("xyz2@gmail.com",observable_iphone)
        

        observable_iphone.add(observer1)
        observable_iphone.add(observer2)
        observable_iphone.add(observer3)

        #observable_iphone.setStockCount(0)
        observable_iphone.setStockCount(100)
    if __name__=="__main__":
        main()
    


