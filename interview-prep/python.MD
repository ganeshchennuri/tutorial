# Basics Python
- Builtin data types, loops, functions, modules
    ```python
    import platform
    platform.architecture() #('64bit', 'WindowsPE')
    platform.python_implementation() # 'CPython'
    ```
- modules like datetime, math, json, re
- Exceptions (try, except, else block, finally)
- String formating
    ```python
    #source w3schools
    # {:.2f} for printing 2 digits after decimal
    myorder = "I want {} pieces of item number {} for {:.2f} dollars."
    print(myorder.format(3, 567, 49))

    myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
    print(myorder.format(3, 567, 49))

    txt = "His name is {1}. {1} is {0} years old."
    print(txt.format(36, 'John'))

    myorder = "I have a {carname}, it is a {model}."
    print(myorder.format(carname = "Ford", model = "Mustang"))
    ```
- classes, oops concepts by [Febin George](https://www.udemy.com/course/python-oops-beginners/)
    ```python
    # class, instance attributes, static & class methods
    # ClassName.attribute => fetching or updating the class attribute
    # obj.attribute => fetching or updating the instance attribute

    # obj.method_name == ClassName.method_name(obj)

    class A():
        def testing(self):
            self.name = "Anton"
            created_by = "Gilfoyle"

    # the parameter created_by only accessible within the method testing, so it cannot be used/modified outside

    # Python supports Single Inheritance, Multiple Inheritance
    # Multilevel Inheritance(methods/attributes are called based on the sequence of inheritance classes if not found in base class

    # Access specifiers & mangling
    # protected: _membername => just a convention, doesn't affect the behavior
    # private: __membername
    class Car:
        number_of_wheels = 4
        _color = "white"
        __year_of_manufacture = 2023 #stored as _Car__year_of_manufacture

    class Bmw(Car):
        def __init__(self):
            print("Protected attribute is:", self._color)
    
    car = Car()
    print("Public attribute is:", car.number_of_wheels)
    bmw = Bmw()
    print("Private attribute is:", bmw._Car__year_of_manufacture)

    # Polymorphism, Overloading is not supported in python
    class Employee():
        def set_working_hours(self):
            self.working_hours = 40
        
        def display_work_hours(self):
            print(self.working_hours)
    

    class Trainee(Employee):
        def set_working_hours(self):
            self.working_hours = 45
        
        def reset_working_hours(self):
            super().set_working_hours()

    # In multiple inheritance, if we have a diamond problem, methods are executed based on MRO(method resolution order)
    # Based on sequence of classes pased while inheriting

    # Operator Overloading, overloading the builtin add operator 
    class Square:
        def __init__(self,side):
            self.side = side
        
        def __add__(sq1,sq2):
            return ((4*sq1.side) + (4*sq2.side))


    # Abstract classes
    # Abstract class can not be instantiated, once inherited forces the Child classes to implement all the abstract methods
    from abc import ABCMeta, abstractmethod

    class Shape(metaclass=ABCMeta):
        @abstractmethod
        def area(self):
            return 0
    
    class Square(Shape):
        side = 4 
        def area(self):
            print("Area of Square: ",self.side * self.side)
        
    class Rectangle(Shape):
        length = 4
        width = 5
        def area(self):
            print("Area of Rectangle: ",self.length * self.width)
    ```
- local, global variables
- File handling, os, sys modules

# Intermediate Python
- Intermediate playlist by [Tech with Tim](https://www.youtube.com/playlist?list=PLzMcBGfZo4-nhWva-6OVh1yKWHBs4o_tv)
    ```python
    # map, filter lambda
    lis = list(range(10))
    print(list(filter(None,lis))) # non zero/empty elements
    print(list(map(lambda x: x*2 if x%2==0 else x*3,lis))) # multiplies by 2 if number is even, 3 if odd
    print(list(filter(lambda x: x%2 == 0,lis))) #filter even numbers from list

    # collections module
    from collections import Counter

    li = [1,2,4,2,1,1,4,5,9,0]
    c = Counter(li) # Counter({1: 3, 2: 2, 4: 2, 5: 1, 9: 1, 0: 1})
    c.elements # <itertools.chain object at 0x0000012E96C49330>
    list(Counter(li).elements()) # [1, 1, 1, 2, 2, 4, 4, 5, 9, 0]
    # c.items(), c.keys(), c.values()
    Counter(li).most_common() #[(1, 3), (2, 2), (4, 2), (5, 1), (9, 1), (0, 1)]

    # Other operations/methods
    c = Counter(a=4,b=2,c=1,d=0)
    d = Counter(a=1,b=0,c=3,d=2)

    c.subtract(d) # Counter({'a': 3, 'b': 2, 'c': -2, 'd': -2})
    c.update(d) # Counter({'a': 4, 'b': 2, 'c': 1, 'd': 0})
    c.clear() # Counter()

    """
    shows elements whose value is above 0
    c + d -> addition of counts 
    c - d -> substraction of counts
    c & d -> intersection
    c | d -> Union
    """

    # namedtuple: like dictionaries, they contain keys that are hashed to a particular value

    # Its like creating class
    Student = namedtuple('Student', ['name', 'age', 'DOB'])
    S = Student('Nandini', '19', '2541997') # Adding value

    print(S[1], S.name, getattr(S, 'DOB'))

    print(S._asdict())

    # Create from dictionary & List
    Student(**dictionary)
    Student._make(li)

    # Additional operations
    S._fields, S._replace(name="Maan")

    print(Student.__new__(Student,"P", 21, "11042001")) # returns new instance of the Student class
    S.__getnewargs__() # returns as plain tuple ('Nandini', '19', '2541997')


    # Deque is preferred over a list in the cases where we need quicker append and pop operations from both the ends of the container
    # deque provides an O(1) time complexity for append and pop operations as compared to a list that provides O(n) time complexity.
    from collections import deque

    myqueue = deque(['name','age','DOB'])
    myqueue.append('Org') #O(1)
    myqueue.appendleft('Full Name')
    myqueue.pop() #O(1)
    myqueue.popleft()
    myqueue.extend(iterable) #O(K), can be extendleft
    myqueue.reverse() #O(N)
    myqueue.rotate(-1) #O(N)
    ```
- Py Coding interviews by [NeetCode](https://www.youtube.com/watch?v=0K_eZGS5NsU)
    ```python
    ord('a') # 97 char to ASCII
    chr(97) # 'a' ASCII to character

    myset = {1,2,3}
    myset.remove(2) # O(1) complexity 

    # tuple can be used as key for hashmap or hashset
    myset = set()
    myset.add((1,2))
    # myset.add([1,3]) => TypeError: unhashable type: 'list'

    # adding as key to dictionary/hashmap
    x = {(i,random.randint(1,10)): i for i in range(1,5)}


    # heapq: heap queue algorithm, also known as the priority queue algorithm
    # Bydefault heaps are minheap in python
    import heapq
    minHeap = []
    heapq.heappush(minHeap,3)
    heapq.heappush(minHeap,2) # similarly 4,6,5

    print(minHeap[0]) #2
    minHeap # [2, 3, 4, 6, 5]
    while len(minHeap):
        # Pops min element each time
        print(heapq.heappop(minHeap))

    # to create maxHeap, multiply by -1, while pushing, popping & accessing

    li = [3, 4, 6, 5, 2]
    heapq.heapify(li) # [2, 3, 6, 5, 4]
    # iterate using while loop to print from smallest to largest


    # Nested functions
    def double(arr, val):
        def helper():
            for i, ele in enumerate(arr):
                arr[i] = ele * 2
            nonlocal val # if update value directly, it will not reflect outside helper function
            val *= 2
        
        helper()
        print(arr, val)

    double([1,2],3)
    ```

# Advanced Python
- Expert Python Techwith Tim [Playlist](https://www.youtube.com/playlist?list=PLzMcBGfZo4-kwmIcMDdXSuy_wSqtU-xDP)
    ```python
    # Python code is compiled to bytecode & then python interpreter runs the bytecode
    # if the code is properly indented & with correct syntax, we can write however we may like it
    # using inspect module we can see all the details related to particular function or clas
    import inspect

    def hello(name):
        def greet():
            print(f"Hello Mr/Ms {name}")
        return greet
    
    greet = hello("John")
    greet()
    print(inspect.getmembers(greet))
    
    # we can also see source code of python modules
    from queue import Queue
    print(inspect.getsource(Queue))

    # Dunder/magic methods
    # we can overide & customize the magic methods, __repr__ representation of obj, __add__ for + operatoe, etc
    ```
- Class defines rules for objects, metclass defines rules for class
    ```python
    # Everything in python is object
    # class is an object of class 'type'
    type(5) #<class 'int'>

    def func():
        pass

    class Test:
        pass
    
    type(func) #<class 'function'>
    type(Test()) #<class '__main__.Test'>
    type(Test) #<class 'type'>

    # we can create class without the class syntax
    Test = type('Test', (), {"x":3}) # equivalent to above definition
    t = Test()
    t.x = 5

    # Inheritance
    class Foo:
        def show(self):
            print("hello world")
    Test = type('Test',(Foo,),{'x':3})

    # adding functions
    def add_attribute(self):
        self.z = 10
    
    Test = type('Test',(Foo,),{'add_attribute':add_attribute})

    # So the class creation is inheriting class type, so if we want to change this
    # Metaclass is the class which allows us to create class unlike the inheritng properties of base class
    class Meta(type):
        def __new__(self, class_name, bases, attributes):
            print(attributes)
            return type(class_name, bases, attributes)

    # if we inherit, it would be simple class, we need to specify as metaclass
    class Dog(metaclass=Meta):
        x = 5
        y = 9
        def hello(self):
            print("hello world")
    # {'__module__': '__main__', '__qualname__': 'Dog', 'x': 5, 'y': 9, 'hello': <function Dog.hello at 0x000002171829B100>}

    # we can also modify the attributes from metclass, before passing to type
    ```
- Decorators
    ```python
    def func(f):
        def wrapper():
            print("started")
            f()
            print("ended")
        return wrapper

    def func2():
        print("finished func2")

    f = func(func2) #passing the func2 as param to func
    f() #calling the returned wrapper

    # two lines can be made as single line if
    @func
    def func3():
        print("finished func3")

    func3() #it automatically calls the function

    # if the functions using decorators have params & unknown number of parameters
    # we can handle by passing *args, **kwargs as params to wrapper function
    # if we want to return the value function returning, we can capture the rv & return
    def func(f):
        def wrapper(*args, **kwargs):
            print(*args, **kwargs)
            rv = f()
            return rv
    
    # extending functionality using decorators
    def timer(func):
        def wrapper(*args, **kwargs):
            st = time.time()
            rv = func(*args, **kwargs)
            et = time.time()
            print("Time: ",et-st)
            return rv

    # Decorator will show the time function took to execute

    # we can also create a logger decorator, it would open & append logging statements to the file
    ```
- Generators
    ```python
    # Generators are a way to generate sequences or values in a memory efficient way,using yield
    # yield keyword pauses execution until next item is requested & keeps track of previous execution
    def gen(n):
        for i in range(n):
            yield i**2
    # find squares of number from 0 to n
    g = gen(1000)
    next(g) #gives the first yielded value

    # manual creation of generator would look like
    class Gen:
        def __init__(self, n):
            self.n = n
            self.last = 0

        def __next__(self):
            return self.next()

        def next(self):
            if self.last == self.n:
                raise StopIteration
            rv = self.last**2
            self.last += 1
            return rv

    g = Gen(1000)
    print(next(g))
    # generator can also be created using ()
    g = (i**2 for i in range(1000))
    ```
- Context managers
    ```python
    # Context managers allow you to ensure a certain operation occurs on exit or crash from a certain block of code

    f = open("file.txt", "r")
    try:
        f.write("hello world")
    finally:
        f.close() #so whatsoever happens while operating on file, it should be closed at end

    # we can do this using the context managers using with keyword
    with open("file.txt", "r") as f:
        f.write("hello world")

    # We can write our context manager
    class File:
        def __init__(self, filename, method):
            self.file = open(filename, method)

        def __enter__(self):
            # returns a value to be used in the context manager
            print("Enter File")
            return self.file

        def __exit__(self, type, value, traceback):
            # ending operation, even if some execption occurs
            print("Exit File", type, value, traceback)
            #<class 'Exception'> Test <traceback object at 0x00000254821E7440>
            self.file.close()
            # return True
            # if we return True, program won't be crashed, but we need to handle the exceptions

    with File('file.txt','w') as f:
        print("Middle")
        f.write('hello world')
        #raise Exception("Test") #even if we raise this, exit method will still be executed

    # context manager can also be created by generator, with decoratot
    from contextlib import contextmanager
    @contextmanager
    def file(filename, method):
        print("Enter")
        f = open(filename, method)
        yield f
        f.close()
        print("Exit")

    with file('file.txt','w') as f:
        f.write("Hello world!")
    ```
- Advance py by [NeuralNine](https://www.youtube.com/playlist?list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc)
    ```python
    # Argument Parsing
    # similar to c language, we can pass arguments while executing python file
    # python main.py hello
    import sys

    filename = sys.argv[0] # main.py
    message = sys.argv[1] # hello

    # we can use len(sys.argv) to fild length or also we can get list of args

    # Capturing optional Parameter like -p for port number, -h for host 
    import getopt
    import sys

    hostip = "0.0.0.0"
    port = 0

    opts, args = getopt.getopt(sys.argv[1:], "h:p:", ["host", "port"])

    print(opts, args)
    for opt, arg in opts:
        if opt == "-h":
            hostip = arg
        elif opt == "-p":
            port = arg

    print(f"Hacking ~->{hostip}:{port}")

    ## Encapsulation
    class P:
        def __init__(self, name, age):
            self.__name = name
            self.__age = age

        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, value):
            self.__name = value


    p = P("Alice", 0)
    print(p.name)
    p.name = "Bob"
    print(p.name)
    ```
- Design patterns
    - Factory Design Pattern [Code](design_patterns/factory.py)
        ```python
        # We would have a factory class/method which would help us creating objects of main class
        # we woud have control over when to create, rather than directly creating an object
        ```
    - Proxy design pattern [Code](design_patterns/proxy.py)
        ```python
        # In proxy patterns, we would have a proxy Class/model, similar to Main CLass, we will customize the methods of main class using proxy class
        # Everything will be hidden behind a proxy Class & acts like a proxy for Main CLass
        ```
    - Singleton design pattern - The closs would only allow instantiation once & uses the object or throws an exception if re-instantiated. Would be helpful in locks, or making the things accessible once at a time.
    - Composite design pattern [Code](design_patterns/composite.py)
        ```python
        # In this example we have Interface/Abstract class for a Department
        # We can have multiple departments in a company and employees in a dept
        # Also we can have ParentDepartment & its employees
        # we can implement interfaces for all these departments & also combine the dept into ParentDepartment.
        
        ```
## Coroutines
- Python functions are also known as a procedure, subprocess, or subroutused for cooperative multitasking of a process that is voluntarily giving away (yield) control over a period of time (periodically).helpers or nested functions in the main function are called subroutines in Python.
- subroutines have only single entry point i.e main function
- Co-routines used for cooperative multitasking of a process that is voluntarily giving away (yield) control over a period of time (periodically).
- Unlike threads, the programmer or programming language decides switching of coroutines.
- CPython uses stack based VM, runtime uses stackpointer for execution. Python Uses Heap for longterm storage
    ```python
    import dis

    def square(x):
        return x*x
 
    def main():
        x = square(4)
        print(x)
        
    dis(square)
    dis(main)
    
    #1           0 RESUME                   0

    #2           2 LOAD_FAST                0 (x)
    #            4 LOAD_FAST                0 (x)
    #            6 BINARY_OP                5 (*)
    
    #1           0 RESUME                   0

    #2            2 LOAD_GLOBAL              1 (NULL + square)
    #3           32 LOAD_GLOBAL              3 (NULL + print)
    #            44 LOAD_FAST                0 (x)
    #            46 PRECALL                  1
    #            60 POP_TOP
    #            62 LOAD_CONST               0 (None)
    #            64 RETURN_VALUE
    ```