class Employee:
    all = []
    def __init__(self, name, salary, manager_name):
        self.name = name
        self.salary = salary
        self.manager_name = manager_name
        Employee.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise AttributeError("Name must be a string")
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if isinstance(salary, int):
            self._salary = salary
        else:
            raise AttributeError("Salary must be an interger")
        
    @property
    def manager(self, manager):
        if isinstance(manager, Manager):
            self._manager = manager
        else:
            raise AttributeError("Manager must be an instance of Manager")
        
    @classmethod
    def paid_over(cls, amt):
        if isinstance(amt, int):
            return [employee for employee in cls.all if employee.salary > amt]
        else:
            raise Exception("Amount paid must be an interger")
        
    @classmethod
    def find_by_department(cls, dept):
        if isinstance(dept, str):
            for employee in cls.all:
                if employee.manager.department == dept:
                    return employee
            return "No employees in that department"
        else:
            raise Exception("Department must be a string")