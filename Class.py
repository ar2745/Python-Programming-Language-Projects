class employee:
    def staff(self, name, salary):
        self.name = name
        self.salary = salary
        print("Employee's name is {} and their salary is {}".format(name, salary))

em = employee()

(em.staff('Paul', 1000))

print(em.name)
print(em.salary)