## Decorator Pattern
> Use when you want to dynamically add new behaviors or responsibilities to an object without modifying its existing structure

### Design a Pizza Ordering System for a restaraunt
The system should allow customers to select a base pizza (e.g., Margherita, Pepperoni, Veggie) and customize it with various toppings (e.g., Cheese, Mushrooms, Olives). Implement the solution using the Decorator pattern to dynamically add toppings to the base pizza and calculate the total cost of the order.

### Solution
The code provided demonstrates the implementation of the Decorator design pattern in Python to represent a pizza ordering system.
The `Pizza` class represents the base pizza object. It has attributes such as **name** and **cost**, and methods to retrieve the pizza's name and cost.

The `ToppingDecorator` class is an abstract class that serves as the base decorator. It inherits from the `Pizza` class and has a reference to a pizza object (self.pizza). It also implements the `get_cost()` and `get_description()` methods, which are delegated to the wrapped pizza object.

Concrete decorator classes like `Cheese`, `Mushrooms`, and `Olives` inherit from ToppingDecorator. Each concrete decorator adds a specific topping to the pizza. These classes override the name and cost attributes of the base decorator class to specify the topping's name and cost.

In the `main()` function or wherever the ordering process occurs, you can create a `base pizza object` (e.g., a margherita pizza). Then, you can wrap it with different decorators (toppings) to customize it. The decorators can be stacked one upon another, and the resulting pizza will have all the toppings applied. Finally, you can retrieve the description and cost of the decorated pizza.

Generic Way to create the decorator layers:

```
bo = BaseObject()

da = DecoratorA(DecoratorB(DecoratorC(bo)))

da.do_something()
```

Here is the output of the above code:

```
---------------------------------
Order Details
---------------------------------
Pizza:  Margherita, Cheese, Mushroom, Olive
Total Cost:  19```