from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def person_method(self):
        """Interface Method"""


class Person(IPerson):
    def person_method(self):
        print("Class Person method")


class ProxyPerson(IPerson):
    def __init__(self) -> None:
        self.person = Person()

    def person_method(self):
        print("Class Proxy Person method")
        self.person.person_method()


p = Person()
p.person_method()

p2 = ProxyPerson()
p2.person_method()
