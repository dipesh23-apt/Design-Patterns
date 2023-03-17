## Singleton Pattern
Singleton provides you with a mechanism to have one, and only one, object of a given type and provides a global point of access. Hence, Singletons are typically used in cases such as logging or database operations, printer spoolers, and many others, where there is a need to have only one instance that is available across the application to avoid conflicting requests on the same resource.<br/>
In brief, the intentions of the Singleton design pattern are as follows:
- Ensuring that one and only one object of the class gets created
- Providing an access point for an object that is global to the program
- Controlling concurrent access to resources that are shared
<br/>

**Implementation**
All implementations of the Singleton have these two steps in common:

- Make the default constructor private, to prevent other objects from using the new operator with the Singleton class.
- Create a static creation method that acts as a constructor. Under the hood, this method calls the private constructor to create an object and saves it in a static field. All following calls to this method return the cached object.

If your code has access to the Singleton class, then it’s able to call the Singleton’s static method. So whenever that method is called, the same object is always returned.<br/>

**Real World Analogy**<br/>
The government is an excellent example of the Singleton pattern. A country can have only one official government. Regardless of the personal identities of the individuals who form governments, the title, “The Government of X”, is a global point of access that identifies the group of people in charge.
<br/>

### Pros and Cons
![chrome_th7LMgrlc3](https://user-images.githubusercontent.com/80080241/225833231-5917de95-38d2-4d16-a16d-7faed159e76c.png)


### Code Explanation in PYTHON
This code implements the `Singleton` design pattern in Python, which ensures that there is only one instance of a class in a program at any given time.

The code defines a metaclass called `SingletonMeta` that will be used to create the Singleton class. The **_instances** class variable in SingletonMeta is a dictionary that will keep track of the instances of classes that use SingletonMeta as their metaclass.

The `__call__` method is called when an instance of a class is created, and is overridden in SingletonMeta to ensure that only one instance of the class is created. It checks whether the class has already been instantiated by looking for it in the _instances dictionary. If the class has not yet been instantiated, it creates a new instance of the class using the `super().__call__()` method, and adds it to the **_instances** dictionary. If the class has already been instantiated, it simply returns the existing instance.

The Singleton class is defined using SingletonMeta as its metaclass. It does not have any specific functionality, but serves as an example of a class that should only have one instance.

The code then creates two instances of the Singleton class, s1 and s2, and compares their ids to see if they are the same. If the ids are the same, it means that only one instance of the class was created, and the program prints _"Singleton works, both variables contain the same instance."_ Otherwise, if the ids are different, it means that two instances of the class were created, and the program prints _"Singleton failed, variables contain different instances."_

When you define a class in Python, Python creates an object of type type to represent that class. This object is an instance of a metaclass. type is the default metaclass in Python, but you can define your own metaclasses by creating a class that inherits from type.
>Output
```
Singleton works, both variables contain the same instance.
<__main__.Singleton object at 0x00000208767B9F70>
```
### Code Explanation in GOLANG

In GO we have goroutines. Hence the singleton struct should return the same instance whenever multiple goroutines are trying to access that instance. It is very easy to get a singleton design pattern wrong. The below code illustrates the right way to create a singleton object. 

In this example, a `sync.Mutex` is used to ensure that only one goroutine at a time can call the **GetInstance()** function. The `mutex.Lock()` call at the beginning of the function acquires the lock, and the `defer mutex.Unlock()` call at the end of the function releases the lock before the function returns.

Note that in this implementation, the **GetInstance()** function is not itself thread-safe. 
The use of `sync.Once` ensures that the initialization code to create the single instance of the Singleton struct is executed only once, even if multiple goroutines call the GetInstance() function simultaneously.
The mutex.Lock() call before the once.Do() call ensures that only one goroutine at a time can execute the initialization code.

Therefore, any number of _goroutines_ can safely call the **GetInstance()** function and use the single instance of the Singleton struct without causing race conditions or other thread-safety issues.

>Output 
```
Creating First Instance
Instance already created
Instance already created
Instance already created
Instance already created
```