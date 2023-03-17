## Design Patterns Concepts
#### Encapsulation:
The key features of encapsulation are as follows:
    <li>An object's behavior is kept hidden from the outside world or objects keep their state information private.
    <li>Clients can't change the object's internal state by directly acting on them; rather, clients request the object by sending messages. Based on the type of requests, objects may respond by changing their internal state using special member functions such as get and set.
    <li>In Python, the concept of encapsulation (data and method hiding)is not implicit, as it doesn't have keywords such as public, private, and protected (in languages such as C++ or Java) that are required to support encapsulation. Of course, accessibility can be made private by prefixing __ in the variable or function name.
#### Polymorphism:
Polymorphism can be of two types:
<li>An object provides different implementations of the method based on input parameters
<li>The same interface can be used by objects of different types
<li>In Python, polymorphism is a feature built-in for the language. For example, the + operator can act on two integers to add them or can work with strings to concatenate them.<br/>
For example(in Python) strings, tuples, or lists can all be accessed with an integer Index.

#### Inheritance:
The following points help us understand the inheritance process better:
<li>Inheritance indicates that one class derives (most of its) functionality from the parent class.
<li>Inheritance is described as an option to reuse functionality defined in the base class and allow independent extensions of the original software implementation.
<li>Inheritance creates hierarchy via the relationships among objects of different classes. Python, unlike Java, supports multiple inheritance (inheriting from multiple base classes).

#### Abstraction:
The key features of abstraction are as follows:
<li>It provides you with a simple interface to the clients, where the clients can interact with class objects and call methods defined in the interface
<li>It abstracts the complexity of internal classes with an interface so that the client need not be aware of internal implementations

#### Composition:
Composition refers to the following points:
<li>It is a way to combine objects or classes into more complex data structures or software implementations
<li>In composition, an object is used to call member functions in other modules thereby making base functionality available across modules without inheritance

## Object Oriented Design Principles
***The Open/Close Principle:*** 
It states that classes or objects and methods should be open for Extension but closed for Modifications<br/>
***The Inversion of Control Principle:***
it states that High Level Modules shouldn't be dependent on Low Level modules;they should both be dependent on `abstraction`.Details should depend on abstraction and not the other way round.<br/>
***The Interface Segregation Principle:***
It states Clients should not be forced to depend on interfaces they don't use.<br/>
***The Single Responsibility Principle:***
it states a Class should have only one reason to change.<br/>
***The Subsitution Principle:***
It states the derived class should completely substitute the base class.<br/>