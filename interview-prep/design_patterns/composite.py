from abc import ABCMeta, abstractmethod


class IDepartment(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, employees):
        """Abstract method"""

    @abstractmethod
    def print_department(self):
        """Abstract Method"""


class Accounting(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting Department: {self.employees}")


class Development(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Development Department: {self.employees}")


class ParentDepartment(IDepartment):
    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add_dept(self, department):
        self.sub_depts.append(department)
        self.employees += department.employees

    def print_department(self):
        print(f"Parent Department Base Employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total Employees: {company.employees}")


if __name__ == "__main__":
    company = ParentDepartment(10)

    accounting = Accounting(40)
    dev = Development(300)
    company.add_dept(accounting)
    company.add_dept(dev)

    company.print_department()
