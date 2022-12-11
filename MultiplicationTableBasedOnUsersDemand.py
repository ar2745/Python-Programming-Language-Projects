num = int(input('Please, choose how many times you want to multiply: '))
for i in range(1, (num + 1)):
    print('\n')
    for k in range(1, 11):
        print(i, '*', k, '=', i*k)