class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.age = 21
        print("Employee's name is {} and their salary is {}".format(name, salary))

class company(employee):
    def staff(self, name, salary):
        employee.__init__(self, name, salary)

class profession(employee):
    def developer(self, name, salary):
        employee.__init__(self, name, salary)

em = company('Hello', 1000)
pr = profession('Andrew', 120000)