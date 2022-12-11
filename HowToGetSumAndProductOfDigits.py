x = abs(int(input("Please type integer values only: ")))

sum = 0
multiple = 1

while x != 0:
    digit = x % 10
    sum += digit
    multiple *= digit

    x = x // 10

print("Sum of digit = ", sum)
print("Product of digit = ", multiple)