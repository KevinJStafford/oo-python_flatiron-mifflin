import ipdb
from lib.employee import Employee

class Manager:
    all = []
    departments = []
    def __init__(self, name, department, age):
        self.name = name
        self.department = department
        self.age = age
        Manager.all.append(name)
        # Manager.departments.append(department)

    def the_employees(self):
        return [e for e in Employee.all if e.manager_name == self]


    def hire_employee(self, employee_name, employee_salary):
        if(isinstance(employee_name, str)
            and isinstance(employee_salary, int)):
            Employee(employee_name, employee_salary, self)
            return f"{self.name} now managing {employee_name}"
        else:
            raise Exception("Name must be a string; salary must be an interger")

    @classmethod
    def all_departments(cls):
        return [manager.department for manager in cls.all]

    @classmethod
    def average_age(cls):
        all_ages = [manager.age for manager in cls.all]
        if all_ages: return round((sum(all_ages) / len(all_ages)),2)   

