num1 = int(input("Please type a number to convert: "))
base_number = int(input("Choose the base:(2-9): "))

if not(2 <= base_number <= 9):
    quit()

num2 = ''

while num1 > 0:
    num2 = str(num1 % base_number) + num2
    num1 //= base_number

print(num2)