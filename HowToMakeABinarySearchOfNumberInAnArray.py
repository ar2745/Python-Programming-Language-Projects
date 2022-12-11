from random import random

N = 20
array = []

for x in range(N):
    array.append(int(random() * 100))

array.sort()
print(array)

number = int(input("Search for any number in array: "))

low = 0
high = N - 1

while low <= high:
    mid = (low + high) // 2

    if number < array[mid]:
        high = mid - 1
    elif number > array[mid]:
        low = mid + 1
    else:
        print("The number is located at index: ", mid)
        break
else:
    print("There is no number!")