from abc import ABC,abstractmethod
class NotificationAlertObserver:
    @abstractmethod
    def update(self):
        pass