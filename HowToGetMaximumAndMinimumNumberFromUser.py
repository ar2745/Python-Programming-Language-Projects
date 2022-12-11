a = int(input('Please, insert first number: '))
b = int(input('Please, insert second number: '))
c = int(input('Please, insert third number: '))

if((a > b) & (a > c)):
    print(a, 'is the greatest number')
elif((b > a) & (b > c)):
    print(b, 'is the greatest number')
else:
    print(c, 'is the greatest number')

#The second method

print(max(a, b, c), 'is the greatest number')