from random import randint

x = 40
array = []

for i in range(x):
    array.append(randint(1, 1000))

for i in array:
    print(i, end=' ')

print()