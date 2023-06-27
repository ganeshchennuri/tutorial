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
- Classes, Oops concepts by [Febin George](https://www.udemy.com/course/python-oops-beginners/)
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
    # protected: _membername => just a convention, doesn;t affect the behavior
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
    set.add((1,2))
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
    # Advanced
    ```