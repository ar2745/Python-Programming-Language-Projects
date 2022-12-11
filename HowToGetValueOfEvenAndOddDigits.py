x = int(input("Please type numbers: "))

e = 0
o = 0

while x > 0:
    if x % 2 == 0:
        e += 1
    else:
        o += 1
    x = x // 10
print("Even numbers = %d, Odd numbers = %d" % (e, o))