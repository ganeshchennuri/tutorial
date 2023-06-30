from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def person_method(self):
        """Interface method for Person"""


class Student(IPerson):
    def __init__(self) -> None:
        self.name = "Student -----"

    def person_method(self):
        print(f"----- {self.name}")


class Teacher(IPerson):
    def __init__(self) -> None:
        self.name = "Teacher -----"

    def person_method(self):
        print(f"----- {self.name}")


def person_factory(person_type):
    if person_type == "Student":
        return Student()
    elif person_type == "Teacher":
        return Teacher()
    else:
        print("Unknown person type")


if __name__ == "__main__":
    choice = input("Please enter Person type: ")
    if obj := person_factory(choice):
        obj.person_method()
