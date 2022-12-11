a = int(input('Please, insert first number: '))
b = int(input('Please, insert second number: '))
c = int(input('Please, insert third number: '))

if((a < b) & (a < c)):
    print(a, 'is the lowest number')
elif((b < a) & (b < c)):
    print(b, 'is the lowest number')
else:
    print(c, 'is the lowest number')

#The second method

print(min(a, b, c), 'is the lowest number')