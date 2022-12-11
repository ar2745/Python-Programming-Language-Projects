str = input("Please type some strings of uppercase and lowercase: ")
len_str = len(str)
upper = lower = 0

for i in str:
    if 'a' <= i <= 'z':
        lower += 1
    elif 'A' <= i <= 'Z':
        upper += 1
print("Percentage of uppercase : %.2f %%" % (upper / len_str * 100))
print("Percentage of lowercase : %.2f %%" % (lower / len_str * 100))
