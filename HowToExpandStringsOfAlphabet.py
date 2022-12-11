str1 = input("Please type starting letter: ")
str2 = input("Please type ending letter: ")

while str1 <= str2:
    print(str1, end=" ")
    str1 = chr(ord(str1) + 1)
print()