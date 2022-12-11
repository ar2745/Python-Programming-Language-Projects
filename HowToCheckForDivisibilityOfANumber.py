x = int(input("Please type the numerator: "))
y = int(input("Please type the denominator: "))

if x % y == 0:
    print(x, "is divisible by", y, "and the answer is:", x / y)
else:
    print(x, "is not divisible by", y)
