def example():
    print("This is our own function")

def hello():
    print("This is another function")

def addition():
    num1 = int(input("Type first number: "))
    num2 = int(input("Type second number: "))
    sum = num1 + num2
    print(sum)

def subtraction():
    num1 = int(input("Type first number: "))
    num2 = int(input("Type second number: "))
    sum = num1 - num2
    print(sum)

def userinput():
    user = input("Please, type your name: ")
    print(user, "thank you for using functions")


print(example())
print(hello())
print(addition())
print(subtraction())
print(userinput())

