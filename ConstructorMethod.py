class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.age = 21
        print("Employee's name is {} and their salary is {}".format(name, salary))

em = employee('Paul', 1000)
print(em.age)
