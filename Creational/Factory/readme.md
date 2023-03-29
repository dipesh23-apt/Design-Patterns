## Factory Pattern
In object-oriented programming, the term factory means a class that is responsible
for creating objects of other types. Typically, the class that acts as a factory has an
object and methods associated with it. The client calls this method with certain
parameters; objects of desired types are created in turn and returned to the client
by the factory.
The Factory Pattern – Building Factories to Create Objects
So the question here really is, why do we need a factory when the client can
directly create an object? The answer is, a factory provides certain advantages
that are listed here:
- The first advantage is loose coupling in which object creation can be
independent of the class implementation.
- The client need not be aware of the class that creates the object which, in turn,
is utilized by the client. It is only necessary to know the interface, methods,
and parameters that need to be passed to create objects of the desired type.
This simplifies implementations for the client.
- Adding another class to the factory to create objects of another type can be
easily done without the client changing the code. At a minimum, the client
needs to pass just another parameter.
• The factory can also reuse the existing objects. However, when the client does
direct object creation, this always creates a new object.
> The Factory helps create objects of different types rather than direct object instantiation.
The following points help us understand the factory method pattern:
- We define an interface to create objects, but instead of the factory being
responsible for the object creation, the responsibility is deferred to the
subclass that decides the class to be instantiated.
- The Factory method creation is through inheritance and not
through instantiation.
- The Factory method makes the design more customizable. It can return the
same instance or subclass rather than an object of a certain type (as in the
simple factory method).


**Implementation**

Make all products follow the same interface. This interface should declare methods that make sense in every product.

Add an empty factory method inside the creator class. The return type of the method should match the common product interface.

In the creator’s code find all references to product constructors. One by one, replace them with calls to the factory method, while extracting the product creation code into the factory method.

You might need to add a temporary parameter to the factory method to control the type of returned product.

At this point, the code of the factory method may look pretty ugly. It may have a large switch statement that picks which product class to instantiate. But don’t worry, we’ll fix it soon enough.

Now, create a set of creator subclasses for each type of product listed in the factory method. Override the factory method in the subclasses and extract the appropriate bits of construction code from the base method.

If there are too many product types and it doesn’t make sense to create subclasses for all of them, you can reuse the control parameter from the base class in subclasses.

For instance, imagine that you have the following hierarchy of classes: the base Mail class with a couple of subclasses: AirMail and GroundMail; the Transport classes are Plane, Truck and Train. While the AirMail class only uses Plane objects, GroundMail may work with both Truck and Train objects. You can create a new subclass (say TrainMail) to handle both cases, but there’s another option. The client code can pass an argument to the factory method of the GroundMail class to control which product it wants to receive.

If, after all of the extractions, the base factory method has become empty, you can make it abstract. If there’s something left, you can make it a default behavior of the method.

![chrome_ZzhqRDWtKK](https://user-images.githubusercontent.com/80080241/228452138-92962275-cb16-41a8-9670-e009ffb96cd7.png)

### Applicability
> Use the Factory Method when you don’t know beforehand the exact types and dependencies of the objects your code should work with.

For example, to add a new product type to the app, you’ll only need to create a new creator subclass and override the factory method in it.
> Use the Factory Method when you want to provide users of your library or framework with a way to extend its internal components.

>  Use the Factory Method when you want to save system resources by reusing existing objects instead of rebuilding them each time.

![chrome_A8UGc2hpy3](https://user-images.githubusercontent.com/80080241/228454487-279c8e08-bcf0-4c07-9b0b-f8b8afbb15d9.png)

### Code Explanation

**Golang**<br/>
It’s impossible to implement the classic Factory Method pattern in Go due to lack of OOP features such as classes and inheritance. However, we can still implement the basic version of the pattern, the Simple Factory.

In this example, we’re going to build various types of weapons using a factory struct.

First, we create the `iGun` interface, which defines all methods a gun should have. There is a `gun` struct type that implements the `iGun` interface. Two concrete guns—`ak47` and `musket`—both embed gun struct and indirectly implement all `iGun` methods.

The `gunFactory` struct serves as a factory, which creates guns of the desired type based on an incoming argument. The `main.go` acts as a client. Instead of directly interacting with ak47 or musket, it relies on gunFactory to create instances of various guns, only using string parameters to control the production.

`go run main.go` wont work
`go run ./` will work

**Golang**<br/>
We create a Creator abstract class that is named Profile. The Profile [Creator] abstract class provides a factory method, createProfile(). 
The *createProfile()* method should be implemented by ConcreteClass to actually create the profiles with appropriate sections. The Profile abstract class is not aware of the sections that each profile should have. For example, a Facebook profile should have personal information and album sections. So we will let the subclass decide this.
We create two ConcreteCreator classes, linkedin and facebook. Each of these classes implement the *createProfile()* abstract method that actually creates
(instantiates) multiple sections (ConcreteProducts) at runtime: