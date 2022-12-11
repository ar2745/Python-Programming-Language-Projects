class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return("Employee's name is: {} and their salary is: {}".format(self.name, self.salary))

class company(employee):
    def __init__(self, name, salary, age):
        employee.__init__(self, name, salary)
        self.age = age

    def __str__(self):
        return (employee.__str__(self) + ' and their age: {}'.format(self.age))

class profession(employee):
    def __init__(self, name, salary, budget):
        employee.__init__(self, name, salary)
        self.budget = budget

    def __str__(self):
        return (employee.__str__(self) + ' and their budget: {}'.format(self.budget))

co = company('Peter', 1000, 21)
pr = profession('James', 500, 1200)

print(co)
print(pr)