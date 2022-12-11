import math

x = float(input("Please type point x: "))
y = float(input("Please type point y: "))
r = float(input("Please type the radius: "))

hypotenuse = math.sqrt(pow(x, 2) + pow(y, 2))

if hypotenuse <= r:
    print("The point belongs to the circle")
else:
    print("The point does not belong to the circle")