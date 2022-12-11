import random

x = []

for i in range(40):
    x.append(int(random.random() * 100))

print(x)

e = o = 0

for i in x:
    if i % 2 == 0:
        e += 1
    else:
        o += 1

print("The number of even = ", e)
print("The number of odd = ", o)