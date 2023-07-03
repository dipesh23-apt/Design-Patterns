class Pizza:
    def __init__(self,name,cost):
        self.name=name
        self.cost=cost
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.name

class ToppingDecorator(Pizza):
    def __init__(self,pizza):
        self.pizza=pizza
    
    def get_cost(self):
        return self.pizza.get_cost()+self.cost
    def get_description(self):
        return self.pizza.get_description()+', '+self.name

class Cheese(ToppingDecorator):
    def __init__(self,pizza):
        super().__init__(pizza)
        self.name='Cheese'
        self.cost=2

class Mushroom(ToppingDecorator):
    def __init__(self,pizza):
        super().__init__(pizza)
        self.name='Mushroom'
        self.cost=3

class Olives(ToppingDecorator):
    def __init__(self,pizza):
        super().__init__(pizza)
        self.name='Olive'
        self.cost=4
