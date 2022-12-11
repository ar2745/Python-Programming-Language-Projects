import random

x = []

for i in range(40):
    x.append(int(random.random() * 20) - 10)

print(x)

positive = []
negative = []

for i in x:
    if i < 0:
        negative.append(i)
    elif i > 0:
        positive.append(i)

print("Negative numbers = ", negative)
print("Positive numbers = ", positive)
