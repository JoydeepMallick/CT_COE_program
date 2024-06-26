# Concept of Lambda functions

⭐⭐Read in detail [here](https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/)

 Lambda Functions are anonymous functions means that the function is without a name.

 ## Difference Between Lambda functions and def defined function
The code defines a cube function using both the ‘def' keyword and a lambda function. It calculates the cube of a given number (5 in this case) using both approaches and prints the results. The output is 125 for both the ‘def' and lambda functions, demonstrating that they achieve the same cube calculation.

```python
def cube(y):
    return y*y*y
 
lambda_cube = lambda y: y*y*y
print("Using function defined with `def` keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))
Output:
```
Output
```
Using function defined with `def` keyword, cube: 125
Using lambda function, cube: 125
```

| With lambda function | Without lambda function |
|----------------------|-------------------------|
| Supports single-line sometimes statements that return some value. |	Supports any number of lines inside a function block |
| Good for performing short operations/data manipulations.|	Good for any cases that require multiple lines of code.|
|Using the lambda function can sometime reduce the readability of code.|	We can use comments and function descriptions for easy readability.|


Various examples depicting implementation:-

### Python Lambda Function with List Comprehension

```python
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
	print(item())
```
Output
```
10
20
30
40
```

### Python Lambda Function with if-else

```python
Max = lambda a, b : a if(a > b) else b
print(Max(1, 2))
```
Output
```
2
```
### Python Lambda with Multiple Statements

```python
List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
sortList = lambda x: (sorted(i) for i in x)
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)
print(res)
```
Output
```
[3, 16, 9]
```
### Using lambda() Function with filter()

```python
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)
```
Output
```
[5, 7, 97, 77, 23, 73, 61]
```
### Using lambda() Function with map()

```python
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x*2, li))
print(final_list)
```
Output
```
[10, 14, 44, 194, 108, 124, 154, 46, 146, 122]
```
### Using lambda() Function with reduce()

```python
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)
```
Output
```
193
```
Here the results of the previous two elements are added to the next element and this goes on till the end of the list like `(((((5+8)+10)+20)+50)+100).`




# Class and Instance concept playlist :-

 🔗[Python OOP Tutorials-Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)

## creating class in python

```python
Class Employee:
    pass # pass is passed when there is no content to be added to a body

emp_1 = Employee() #initialized constructor pass parameters if any

emp_1.name = "Galen Colin"
emp_1.pay = 45000

print(emp_1.name)
```
Output
```
Galen Colin
```


### Creating constructor in python

```python
    Class class_name:
        def __init__(self, param1, param2):
            self.param1 = param1
            self.param2 = param2
```

## importance of self      

The `self` parameter in Python is a reference to the **current instance of the class** and is used to access variables and methods that belongs to the class. It is not a keyword but rather a conventionally used naming convention for the first parameter of a method in a class.

When a method is called, Python passes the instance of the class as the first argument to the method. This is why you often see self as the first parameter in method definitions.

## How to access class methods

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Jack', 'Jones', 1200)

# Method 1
print(emp1.fullname())

# Method 2
print(Employee.fullname(emp1))

```

Output:-
```
Jack Jones
Jack Jones
```

- Method 1: Preferred in most situations due to its simplicity and readability. **Instance Method Call** The instance is implicitly passed as the self argument.

- Method 2: Can be useful for educational purposes or for certain metaprogramming techniques, but generally not used in everyday programming. **Class Method Call with Instance** The instance is explicitly passed as the self argument.

## Class variables

```python
class Employee:
    rate = 1.07

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def raise_pay(self):
        self.pay = int(self.pay * rate)

emp1 = Employee('Jack', 'Jones', 1200)

print(emp1.pay)
emp1.raise_pay()
print(emp1.pay)

```

Output 
```
Error : rate is not defined
```
i.e. variable must either be accessed via class or instance.

Correction needed :-
```python
...
...
    def raise_pay(self):
        self.pay = int(self.pay * Employee.rate)
...
...
```

Another example

```python
class Emp:
    emp_cnt = 0
    def __init__(self):
        Emp.emp_cnt += 1

print(Emp.emp_cnt)
emp1 = Emp()
emp2 = Emp()
print(Emp.emp_cnt)
```

Output:-
```
0
2
```

## __dict__ attribute usecase

The `__dict__` attribute in Python refers to the dictionary of an object’s (writable) attributes. This attribute is a dictionary that stores the object’s attributes, which can be accessed using the dot notation.

Here’s an example of how to use the __dict__ attribute:
```python
class MyClass:
    def __init__(self):
        self.a = 1
        self.b = 2

obj = MyClass()
print(obj.__dict__)
print(MyClass.__dict__)
```
Output:
```
{'a': 1, 'b': 2}

mappingproxy({'__module__': '__main__', '__init__': <function MyClass.__init__ at 0x000001A6F3ECF240>, '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None})
```

## Class method using @classmethod decorator

- A class method is a method that is bound to the class and not the object of the class.
- They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
- It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that would be applicable to all instances.

Read more :- [here](https://www.geeksforgeeks.org/classmethod-in-python/)

Using classmethod as constructor

```python
class Emp:
    @classmethod
    def from_string(cls, empstring):
        first, last, pay = empstring.split('-')
        return cls(first, last, pay) #return emp object

empstr1 = "Jane-Doe-20000"
emp1 = Emp.from_string(empstr1)
print(emp1.pay)
```

Output :
```
20000
```

### cls parameter

The cls parameter in Python is a conventionally used parameter in class methods. It refers to the class itself and is typically the first parameter passed to a class method. This means that when you call a class method, the class is automatically passed as the first argument to the method, and you can access it through the cls parameter.

Here is an example of how to use cls in a class method:

```python
class MyClass:
    @classmethod
    def my_method(cls):
        print(cls)

MyClass.my_method()
```

Output
```
 <class '__main__.MyClass'>
```
## Static method using @staticmethod decorator

They **do not** have to any instance i.e. `self`/class i.e.`cls` as paramter unlike classmethods.

- A class method takes cls as the first parameter while a static method needs no specific parameters.
- A class method can access or modify the class state while a static method can’t access or modify it.
- In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
- We use @classmethod decorator in Python to create a class method and we use @staticmethod decorator to create a static method in Python.

```python
class Emp:
    @staticmethod
    def isworkday(day):
        return day.weekday() != 5 or day.weekday() != 6

import datetime
dt = datetime.date(2016, 7, 10) #sunday
print(Emp.isworkday(dt))

```

Output
```
False
```

## Inheritance


```python
class Employee:
    rate = 1.07
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def raise_pay(self):
        self.pay = int(self.pay * rate)

class Dev(Employee):
    def __init__(self, first, last, pay, prog):
        # method 1
        super().__init__(first, last, pay)
        # method 2
        Employee.__init__(self, first, last, pay)
        self.prog = prog

emp1 = Employee('Jack', 'Jones', 12000)
dev2 = Dev('Maria', 'Jones', 50000, 'HTMX')
print(help(dev2)) # helps gaining info about Dev object
```
Output :

```
Help on Dev in module __main__ object:

class Dev(Employee)
 |  Dev(first, last, pay, prog)
 |
 |  Method resolution order:
 |      Dev
 |      Employee
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, first, last, pay, prog)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from Employee:
 |
 |  fullname(self)
 |
 |  raise_pay(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Employee:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
-- More  --
```

Lets create another subclass:-

```python
class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self ,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self ,emp):
        if emp in self.employees:
            self.employees.remove(emp)

dev1 = Dev('Maria', 'Jones', 50000, 'HTMX')
mgr1  = Manager("Koris", "Kane", 1000, [dev1])
print(mgr1.employees)
dev2 = Dev('Shoruld', 'Arin', 9000, 'Erlang')
mgr1.add_emp(dev2)
print(mgr1.employees)
```

Output
```
[<__main__.Dev object at 0x00000244A8D75730>]
[<__main__.Dev object at 0x00000244A8D75730>, <__main__.Dev object at 0x00000244A8C2A390>]
```

## isintance function

syntax : `isinstance(instancename, classname)`

```python
isinstance(mgr1, Employee)
isinstance(mgr1, Dev)
```

Output : 
```
True
False
```

## issubclass function

syntax : `issubclass(childclassname, parentclassname)`

```python
issubclass(Manager, Employee)
issubclass(Manager, Dev)
```

Output : 
```
True
False
```


## dunder methods or magic methods

Python’s magic methods or dunder methods are special methods that have **double underscores (or “dunder”)** at the beginning and end of their names. These methods provide a way to define specific behaviors for built-in operations or functionalities in Python classes. They are used to overload operators, implement functions, and customize object behavior.

Here are some examples of dunder methods:

1. ` __init__`: Initializes the object when it’s created.
2. `__str__`: Returns a string representation of the object.
3. `__add__`: Defines how two objects are added together.
4. `__contains__`: Checks if an object is contained within another.
5. `__getitem__`: Defines how objects are indexed.
6. `__setitem__`: Defines how objects are set.
7. `__delitem__`: Deletes an item from an object.
8. `__len__`: Returns the length of an object.
9. `__repr__`: Returns a machine-readable representation of the object.
10. `__eq__`: Checks if two objects are equal.



For info on `__repr__` vs `__str__` read [here](https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr)

read more on magic method [here](https://rszalski.github.io/magicmethods/)

### `__repr__` usecase



It simple beautifies or personalizes what we see when we print an object

Goal is to be unambigous

```python
class Employee:
    rate = 1.07
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def raise_pay(self):
        self.pay = int(self.pay * rate)
    def __repr__(self):
        return "Employee object({}, {}, {})".format(self.first, self.last, self.pay)

emp1 = Employee("Kaley", "Hajdin", 78000)
print(emp1) # same as emp1.__repr__
```

Output

```
Employee object(Kaley, Hajdin, 78000)
```

### `__str__` usecase

Similar to repr and aids readability

When both used `__str__` is defaultly shown

```python
class Employee:
    rate = 1.07
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def raise_pay(self):
        self.pay = int(self.pay * rate)
    def __repr__(self):
        return "Employee object({}, {}, {})".format(self.first, self.last, self.pay)
    def __str__(self):
        return "Employee {} {} with pay {}".format(self.first, self.last, self.pay)

emp1 = Employee("Kaley", "Hajdin", 78000)
print(emp1) # same as emp1.__str__
```

Output

```
Employee Kaley Hajdin with pay 78000
```

### `__add__` usecase

```python
print(1+2)
# same as
print(int.__add__(1+2))

print('a'+'b')
# same as
print(str.__add__('a'+'b'))
```
Output
```
3
3
ab
ab
```

Using it to add 2 objects

```python
class Employee:
    rate = 1.07
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def raise_pay(self):
        self.pay = int(self.pay * rate)
    def __add__(self, other):
        return self.pay + other.pay

emp1 = Employee("Fa","Me", 23000)
emp2 = Employee("Jack", "Sparrow", 27000)
print(emp1 + emp2)
```
Output
```
50000
```

### `__len__` usecase

Same as `len(variable)`

```python
class Employee:
    rate = 1.07
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def raise_pay(self):
        self.pay = int(self.pay * rate)
    def __len__(self):
        return len(self.first) + len(self.last)
    
emp1 = Employee("Fa", "Me", 78000)
print(len(emp1))
```
Output
```
4
```

# Polymorphism

The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function.

```python
# len() being used for a string
print(len("geeks"))
 
# len() being used for a list
print(len([10, 20, 30]))
```
Output
```
5
3
```
Polymorphism in class methods
```python
class Animal:
	def speak(self):
		raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
	def speak(self):
		return "Woof!"

class Cat(Animal):
	def speak(self):
		return "Meow!"

# Create a list of Animal objects
animals = [Dog(), Cat()]

# Call the speak method on each object
for animal in animals:
	print(animal.speak())
```
Output
```
Woof!
Meow!
```

# Encapsulation

idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.

A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc. The goal of information hiding is to ensure that an object’s state is always valid by controlling access to attributes that are hidden from the outside world.

## protected members

Protected members (in C++ and JAVA) are **those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses**. 

To accomplish this in Python, just follow the convention by **prefixing the name of the member by a single underscore “_”**.

```python
# Creating a base class 
class Base: 
	def __init__(self): 
		# Protected member 
		self._a = 2

# Creating a derived class 
class Derived(Base): 
	def __init__(self): 
		Base.__init__(self) 
		print("Calling protected member of base class: ", self._a) 
		# Modify the protected variable: 
		self._a = 3
		print("Calling modified protected member outside class: ", self._a) 

obj1 = Derived() 
obj2 = Base() 

# Calling protected member 
# Can be accessed but should not be done due to convention 
print("Accessing protected member of obj1: ", obj1._a) 

# Accessing the protected variable outside 
print("Accessing protected member of obj2: ", obj2._a) 
```
Output
```
Calling protected member of base class:  2
Calling modified protected member outside class:  3
Accessing protected member of obj1:  3
Accessing protected member of obj2:  2
```
Accessing it as a class variable is not possible.
```python
Base._a
```
Output
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Base' has no attribute '_a'
```

## Private members
Private members are similar to protected members, the difference is that the **class members declared private should neither be accessed outside the class nor by any base class**. In Python, there is no existence of Private instance variables that cannot be accessed except inside a class.

However, to define a private member **prefix the member name with double underscore “__”**.

Note: Python’s private and protected members can be accessed outside the class through python name [mangling](https://www.geeksforgeeks.org/private-variables-python/). 

```python
class Base: 
    def __init__(self): 
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
  
# Creating a derived class 
class Derived(Base): 
    def __init__(self):  
        Base.__init__(self) 
        print("Calling private member of base class: ") 
        print(self.__c) 

obj1 = Base() 
print(obj1.a) 
```
Output
```
GeeksforGeeks
```

Possible errors :-
```python
print(obj1.c)
```
Output
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Base' object has no attribute 'c'
```

```python
# private member of base class 
# is called inside derived class 
obj2 = Derived()
```
Output
```
Calling private member of base class:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in __init__
AttributeError: 'Derived' object has no attribute '_Derived__c'
```

# Abstraction

Abstraction is used to hide the internal functionality of the function from the users. **The users only interact with the basic implementation of the function, but inner working is hidden.** User is familiar with that "what function does" but they don't know "how it does."

In Python, abstraction can be achieved by using abstract classes and interfaces. **Python provides the abc module to use the abstraction in the Python program.**

- An Abstract class can contain the both method normal and abstract method.
- An Abstract cannot be instantiated; we cannot create objects for the abstract class.

## Abstract Base Classes
An abstract base class is the common application program of the interface for a set of subclasses. It can be used by the third-party, which will provide the implementations such as with plugins. It is also beneficial when we work with the large code-base hard to remember all the classes.

## Working of the Abstract Classes
Unlike the other high-level language, **Python doesn't provide the abstract class itself**. We need to import the abc module, which provides the base for defining **Abstract Base classes (ABC)**. The ABC works by decorating methods of the base class as abstract. It registers concrete classes as the implementation of the abstract base. We use the `@abstractmethod` decorator to define an abstract method or if we don't provide the definition to the method, it automatically becomes the abstract method. 

```python
from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
t= Tesla ()   
t.mileage()    
  
s = Suzuki()   
s.mileage()   
```
Output
```
The mileage is 30kmph
The mileage is 25kmph 
```
In the above code, we have imported the abc module to create the abstract base class. We created the Car class that inherited the ABC class and defined an abstract method named mileage(). We have then inherited the base class from the three different subclasses and implemented the abstract method differently. We created the objects to call the abstract method.

# File Handling 

Basic concepts :- [readme](https://www.w3schools.com/python/python_file_handling.asp)

Reading files :- [readme](https://www.w3schools.com/python/python_file_open.asp)

Writing files :- [readme](https://www.w3schools.com/python/python_file_write.asp)

Deleting files and folders using os module :- [readme](https://www.w3schools.com/python/python_file_remove.asp)

# Exception handling

In Python, there are several built-in Python exceptions that can be raised when an error occurs during the execution of a program. Here are some of the most common types of exceptions in Python:

1. `SyntaxError`: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
2. `TypeError`: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
3. `NameError`: This exception is raised when a variable or function name is not found in the current scope.
4. `IndexError`: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
5. `KeyError`: This exception is raised when a key is not found in a dictionary.
6. `ValueError`: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
7. `AttributeError`: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
8. `IOError`: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
9. `ZeroDivisionError`: This exception is raised when an attempt is made to divide a number by zero.
10. `ImportError`: This exception is raised when an import statement fails to find or load a module.


These are just a few examples of the many types of exceptions that can occur in Python. It’s important to handle exceptions properly in your code using try-except blocks or other error-handling techniques, in order to gracefully handle errors and prevent the program from crashing.

## Error vs Exception

[readme](https://www.geeksforgeeks.org/errors-and-exceptions-in-python/?ref=lbp)

Errors are the problems in a program due to which the program will stop the execution. 

On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program. 
Two types of Error occurs in python. 
 

1. Syntax errors : colon missing after if, wrong indention
2. Logical errors (Exceptions) :dividing number by 0, accessing element of array of out index

## Catching exceptions

Try and except statements are used to catch and handle exceptions in Python.

```python
a = [1, 2, 3]
try: 
	print ("Second element = %d" %(a[1]))
	print ("Fourth element = %d" %(a[3]))
except:
	print ("An error occurred")
```
Output
```
Second element = 2
An error occurred
```

## Catching specific exception

```python
def fun(a):
	if a < 4:
		b = a/(a-3)
	print("Value of b = ", b)
	
try:
    #comment either one from below
	fun(3) # see output 1
	fun(5) # see output 2
except ZeroDivisionError:
	print("ZeroDivisionError Occurred and Handled")
except NameError:
	print("NameError Occurred and Handled")
```
Output 1 : Obvious
```
ZeroDivisionError Occurred and Handled
```
Output 2 : b inaccessible before print
```
NameError Occurred and Handled
```

## Try with Else Clause

In Python, you can also use the else clause on the try-except block which must be present after all the except clauses. 

**The code enters the else block only if the try clause does not raise an exception.**

```python
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
```
Output
```
-5.0
a/b result in 0 
```

## Finally keyword
always executed after the try and except blocks. Always executes irrespective of exception occurs or not.

```python
try:
	k = 5//0
	print(k)

except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	print('This is always executed')
```
Output
```
Can't divide by zero
This is always executed
```

## Raising exceptions

The raise statement allows the programmer to force a specific exception to occur. The sole argument in raise indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from Exception).

```python
try: 
	raise NameError("Hi there")
except NameError:
	print ("An exception")
	raise
```
Output
```
Traceback (most recent call last):
  File "/home/d6ec14ca595b97bff8d8034bbf212a9f.py", line 5, in <module>
    raise NameError("Hi there")  # Raise Error
NameError: Hi there
```

# Exceptions

## Built-in exceptions
⭐⭐Definitely read this article :- [readme](https://www.geeksforgeeks.org/built-exceptions-python/?ref=lbp)

There are several built-in exceptions in Python that are raised when errors occur. These built-in exceptions can be viewed using the local() built-in functions as follows :
```python
locals()['__builtins__']
```
## User-defined exceptions


⭐⭐Definitely read in detail [here](https://www.geeksforgeeks.org/user-defined-exceptions-python-examples/?ref=lbp)

Exceptions need to be derived from the Exception class, either directly or indirectly. Although not mandatory, most of the exceptions are named as names that end in “Error” similar to the naming of the standard exceptions in python.

```python
class MyError(Exception):

	# Constructor or Initializer
	def __init__(self, value):
		self.value = value

	# __str__ is to print() the value
	def __str__(self):
		return(repr(self.value))


try:
	raise(MyError(3*2))

# Value of Exception is stored in error
except MyError as error:
	print('A New Exception occurred: ', error.value)
```
Output
```
A New Exception occurred:  6
```

# Python Logging

⭐⭐Read in detail [here](https://www.datacamp.com/tutorial/logging-in-python)

logging is a way of keeping a log generated from a computer program. A log file usually has a set of records of events that occur in your code ( for example, a python code ) or an operating system. These events or messages are written to a log file, a message, or an event can also be a communication between different users.

Five Levels of Logging as shown here, are:

![](https://images.datacamp.com/image/upload/f_auto,q_auto:best/v1584715062/logging1_sjhzzn.png)

- Debug (10): Useful for diagnosing issues in the code.

- Info (20): It can act as an acknowledgment that there are no bugs in the code. One good use-case of Info level logging is the progress of training a machine learning model.

- Warning (30): Indicative of a problem that could occur in the future. For example, a warning of a module that might be discontinued in the future or low-ram warning.

- Error (40): A serious bug in the code, could be a syntax error, out of memory error, exceptions.

- Critical (50): An error due to which the program might stop functioning or might exit abruptly.

Important logging attributes for reference :-

![](https://images.datacamp.com/image/upload/f_auto,q_auto:best/v1584715063/logging5_ugwysb.png)

Read more [here](https://www.geeksforgeeks.org/logging-in-python/)

### 🙄  quite confused regarding logging yet. 


# Python regex

Very good videos :-

🔗[Corey Schafer general regex](https://www.youtube.com/watch?v=sa-TUpSx1JA)

🔗[Corey schafer python regex](https://www.youtube.com/watch?v=K8L6KVGG-7o)

For quick read see [w3school](https://www.w3schools.com/python/python_regex.asp) and [GFG](https://www.geeksforgeeks.org/regular-expression-python-examples/)

A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

Python has a built-in package called `re`, which can be used to work with Regular Expressions.

# Multithreading in python

A program in execution is known as a **process**. When you start any app or program on your computer, such as the internet browser, the operating system treats it as a process.

a **thread** is synonymous with lightweight processes.a thread is a sequence of instructions that the computer performs. It is executed independently.

To facilitate multithreading in Python, we can make use of the following modules offered by Python –

- Thread Module
- Threading Module

[readme](https://www.scaler.com/topics/multithreading-in-python/)

Multithreading in Python is a popular technique that enables multiple tasks to be executed simultaneously. In simple words, the ability of a processor to execute multiple threads simultaneously is known as multithreading.

## 1. Using the Threading Module
Let's take a look at the code using which we can create a new thread using the Threading Module –

```python
from threading import *
def MyThread1():
    print("I am in thread1.", "Current Thread in Execution is", current_thread().getName())
def MyThread2():
    print("I am in thread2.", "Current Thread in Execution is", current_thread().getName())
t1 = Thread(target=MyThread1, args=[])
t2 = Thread(target=MyThread2, args=[])
t1.start()
t2.start()
```
Output:
```
I am in thread1. Current Thread in Execution is Thread-1
I am in thread2. Current Thread in Execution is Thread-2
```

## 2. Using the Thread Module

The way to create a new thread using the Thread module is as follows –

```python
import _thread
def MyThread1():
    print("This is thread1")
def MyThread2():
    print("This is thread2")
 
_thread.start_new_thread(MyThread1, ())
_thread.start_new_thread(MyThread2, ())
```

Output:
```
This is thread1
This is thread2
```

**Note**: The output of the above code snippet can differ for different runs. It happens because multithreading in Python using the _thread module is unstable.

No one can tell which thread is going to get executed first. The _thread module treats threads as functions while the Threading module is implemented in an object-oriented way, which means every thread corresponds to an object. The _thread module has also been deprecated and is only used for backward incompatibilities in Python3.

Out of the two methods, the recommended one is using the Threading module.

 The Threading module is preferred as its intuitive APIs help us synchronize thread executions, thus making it predictable and highly reliable.

More complex concepts like synchronization, multithreaded priority queue discussed [here](https://www.tutorialspoint.com/python/python_multithreading.htm)


# Multiprocessing in python

Explained in detail [here](https://www.analyticsvidhya.com/blog/2021/04/a-beginners-guide-to-multi-processing-in-python/)

Multiprocessing refers to the ability of a system to support more than one processor at the same time. Applications in a multiprocessing system are broken to smaller routines that run independently. The operating system allocates these threads to the processors improving performance of the system.

![](https://editor.analyticsvidhya.com/uploads/53591Screenshot%202021-04-25%20at%207.55.24%20PM.png)

![](https://editor.analyticsvidhya.com/uploads/44715Screenshot%202021-04-25%20at%207.55.35%20PM.png)




| Multithreading	| Multiprocessing |
|-------------------|-----------------|
| It is a technique where a process spawns multiple threads simultaneously. |It is the technique where multiple processes run across multiple processors/processor cores simultaneously. |
|Python multithreading implements concurrency.	|Python multiprocessing implements parallelism in its truest form.
|It gives the illusion that they are running parallelly, but they work in a concurrent manner.|	It is parallel in the sense that the multiprocessing module facilitates the running of independent processes parallelly by using subprocesses.|
|In multithreading, the GIL or Global Interpreter Lock prevents the threads from running simultaneously.| In multiprocessing, each process has its own Python Interpreter performing the execution.|

![](https://scaler.com/topics/images/multithreading-and-multiprocessing-in-python.webp)

# Test file concept

Read more [here](https://realpython.com/python-testing/)

- exploratory testing and is a form of manual testing. Exploratory testing is a form of testing that is done without a plan. In an exploratory test, you’re just exploring the application.

-  Automated testing is the execution of your test plan (the parts of your application you want to test, the order in which you want to test them, and the expected responses) by a script instead of a human. Python already comes with a set of tools and libraries to help you create automated tests for your application.

- testing multiple components is known as integration testing. A major challenge with integration testing is when an integration test doesn’t give the right result. It’s very hard to diagnose the issue without being able to isolate which part of the system is failing. 

- A unit test is a smaller test, one that checks that a single component operates in the right way. A unit test helps you to isolate what is broken in your application and fix it faster.

## test runners available

There are many test runners available for Python. The one built into the Python standard library is called unittest. 

The principles of unittest are easily portable to other frameworks. The three most popular test runners are:

### 1. [unittest](https://realpython.com/python-testing/#unittest)
unittest has been built into the Python standard library since version 2.1. unittest requires that:

- You put your tests into classes as methods
- You use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement

(check the link to know more regarding example)

### 2. [nose or nose2](https://realpython.com/python-testing/#nose)

nose is compatible with any tests written using the unittest framework and can be used as a drop-in replacement for the unittest test runner. The development of nose as an open-source application fell behind, and a fork called nose2 was created. If you’re starting from scratch, it is recommended that you use nose2 instead of nose.

(check more in documentation)

### 3. [pytest](https://realpython.com/python-testing/#pytest)

pytest supports execution of unittest test cases. The real advantage of pytest comes by writing pytest test cases. **pytest test cases are a series of functions in a Python file starting with the name test_.**

pytest has some other great features:

- Support for the built-in assert statement instead of using special `self.assert*()` methods
- Support for filtering for test cases
- Ability to rerun from the last failing test
- An ecosystem of hundreds of plugins to extend the functionality

```python
#filename test_example.py
def test_pass():
    assert 2 < 3
```
In terminal
```bash
pytest
```
Output
```
 H:\_MyProjects_\3rd year\CT_COE_program\Week 2 27.5.24 to 1.6.24> pytest
===================================== test session starts =====================================
platform win32 -- Python 3.10.0, pytest-7.2.2, pluggy-1.0.0
rootdir: H:\_MyProjects_\3rd year\CT_COE_program\Week 2 27.5.24 to 1.6.24
collected 1 item

test_example.py .                                                                        [100%] 

====================================== 1 passed in 0.23s ====================================== 
```

## structuring a test

check this [video](https://www.youtube.com/watch?list=PLJsmaNFr5mNqSeuNepT3IaMrgzRMm9lQR&v=sCthIEOaMI8)

Arrange, act, assert methodology

```python
#filename test_example2.py
def greet(person):
    return "hi {name}".format(**person)

def test_greet():
    bob = {"name": "Bob"}       # Arrange
    greeting = greet(bob)       # Act
    assert greeting == "hi Bob" # Assert
```
In terminal
```bash
pytest .\test_example2.py
```
Output
```
===================================== test session starts =====================================
platform win32 -- Python 3.10.0, pytest-7.2.2, pluggy-1.0.0
rootdir: H:\_MyProjects_\3rd year\CT_COE_program\Week 2 27.5.24 to 1.6.24
collected 1 item

test_example2.py .                                                                       [100%] 

====================================== 1 passed in 0.09s ======================================
```

## pytest fixtures

⭐⭐⭐Read in detail [here](https://www.geeksforgeeks.org/fixtures-in-pytest/)


Pytest fixtures are a powerful feature that allows you to set up and tear down resources needed for your tests. They help in creating reusable and maintainable test code by providing a way to define and manage the setup and teardown logic. 

A Fixture is a piece of code that runs and returns output before the execution of each test.

**Syntax:**
```python
# Importing the math and pytest libraries 
import math 
import pytest 

# Creating the common function for input 
@pytest.fixture 
def input_value(): 
    input = 8
    return input

# Creating first test case 
def test_check_difference(input_value): 
    assert 99-93==input_value 

# Creating second test case 
def test_check_square_root(input_value): 
    assert input_value==math.sqrt(64)

```

Its kind of like 1 test for multiple functions.

e.g.
```py
import pytest

@pytest.fixture
```
Output:
```pwsh
==================================== test session starts =====================================
platform win32 -- Python 3.10.0, pytest-7.2.2, pluggy-1.0.0
rootdir: H:\_MyProjects_\3rd year\CT_COE_program\Week 2 27.5.24 to 1.6.24
collected 2 items

pytest_fixture_example.py F.                                                            [100%]

========================================== FAILURES ========================================== 
___________________________________ test_check_difference ____________________________________

input_value = 8

    def test_check_difference(input_value):
>       assert 99-93==input_value
E       assert (99 - 93) == 8

pytest_fixture_example.py:13: AssertionError
================================== short test summary info ===================================
FAILED pytest_fixture_example.py::test_check_difference - assert (99 - 93) == 8
================================ 1 failed, 1 passed in 1.18s ================================= 
```

## mock patching a function


Read [here](https://www.fugue.co/blog/2016-02-11-python-mocking-101) and also [here](https://realpython.com/python-mock-library/)

**Mocking** = "The replacement of one or more function calls or objects with mock calls or objects"

A mock function call returns a predefined value immediately, without doing any work. A mock object's attributes and methods are similarly defined entirely in the test, without creating the real object or doing any work. 

In Python, mocking is accomplished through the `unittest.mock` module. The module contains a number of useful classes and functions, the most important of which are the `patch` function (as decorator and context manager) and the `MagicMock` class. Mocking in Python is largely accomplished through the use of these two powerful components.

### 🙄quite confused regarding the same.