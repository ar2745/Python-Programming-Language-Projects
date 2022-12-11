x = int(input("Please type some numbers: "))
y = 0
z = x

while x != 0:
    digit = x % 10
    x = x // 10
    y = y * 10
    y = y + digit
print("The reversed of", z, "=", y)