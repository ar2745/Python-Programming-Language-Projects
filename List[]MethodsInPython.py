a = ['Paul', 'Peter', 'Hello', 93, 73, 102]
b = ['Paul', 'Peter', 'Hello', 93, 73, 102]
c = ['Paul', 'Peter', 'Hello', 93, 73, 102]
z = ['Paul', 'Peter', 'Hello', 93, 73, 102]
print(a)

for i in a:
    print(i)

a.append('Andrew')
a.append('Thomas')

print(a)

a.remove('Thomas')

print(a)

print(a.index('Peter'))
print(a)

a.reverse()

print(a)
print(a.pop(1))
print(a.count('Peter'))

a.append('Peter')

print(a.count('Peter'))

print(dir())