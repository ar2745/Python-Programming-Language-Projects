a = int(input("Please type first number: "))
b = int(input("Please type second number: "))

try:
    c = a / b
except:
    print("You cannot divide", a, "by", b)
else:
    print(c)
