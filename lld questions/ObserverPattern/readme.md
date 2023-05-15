## Design an Amazon notification system that sends notifications to subscribed users when a product's stock becomes available. 

## Observer Pattern
The above code demonstrates the Observer Pattern in Python, which is a behavioral design pattern that allows one or more objects to observe changes in the state of another object.



### The code is divided into two parts and 5 files
- Observable
  - IphoneObservable.py
  - StockObservable.py
- Observer
  - EmailAlertObservable.py
  - MobileAlertObservable.py
  - NotificationAlertObservable.py
- store.py

## Class Diagram
Sure, here's a class diagram for a basic implementation of an Amazon notification system based on the Observer pattern:
![chrome_0Cx4r6Gpuy](https://github.com/dipesh23-apt/Design-Patterns/assets/80080241/5be81ec5-b052-451f-9235-6eb8c92e2e52)



The `StockObservable` is an interface that represents the subject of the observer pattern.<br/> It has methods: `add()` and `remove()` observers `notifySubscriber()` to notify all the attached observers and the getter & setter methods `setStockCount()`  `getStockCount` .

The `IphoneObservable` class is a concrete implementation of **StockObservable** and adds a `observerList` and `stockCount`in the constructor.

The `NotificationObserver` is the observer **interface** which defines the update method that will be called by the subject when the stock_count changes.

The `EmailAlertObserver` is a concrete implementation of the **NotificationObserver** that sends an email notification to the subscribed email address. It has an `email` field and an object of **StockObservable** and `sendmail()` function to send a mail

The `MobileAlerObserver` is a concrete implementation of the **NotificationObserver** that sends an message notification to the subscribed phone number. It has an `phone` field and an object of **StockObservable** and `sendmsg()` to send a message.
