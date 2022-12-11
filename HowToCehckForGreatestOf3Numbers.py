x = int(input("Please type first number: "))
y = int(input("Please type second number: "))
z = int(input("Please type third number: "))

print("The maximum number is: ", end="")

if y <= x >= z:
    print(x)
elif x <= y >= z:
    print(y)
else:
    print(z)