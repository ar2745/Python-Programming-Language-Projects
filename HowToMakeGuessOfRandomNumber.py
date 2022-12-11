from random import randint

guess_num = randint(1, 100)
user_input = -1
trial_period = 1

while guess_num != user_input:
    print("The trial no %d: " % trial_period, end='')
    user_input = int(input())
    if user_input < guess_num:
        print("The input number is less")
    elif user_input > guess_num:
        print("The input number is more")
    else:
        print("Kudos! The right guess!")
        exit(0)
    trial_period += 1

    if trial_period > 7:
        print("Sorry you exceeded the amount of attempts to guess the right number")
        print("The appropriate integer is", guess_num)
        exit(0)