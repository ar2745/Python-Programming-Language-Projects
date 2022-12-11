n = 'Hello'
a = 21
g = 95

print("Student\'s name is", n, "and their age is", a, "and their grade is", g)
print("Student\'s name is {} and their age is {} and their grade is {}" .format(n, a, g))

for i in range(1, 11):
    print("{:5} {:5} {:5}".format(i, i * i, i * i *i))