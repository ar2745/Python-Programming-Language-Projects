password = 'password'
for a in range(3):
    psw = input('Enter password: ')
    b = 2
    if(psw == password):
        print('Access Granted')
        break
    else:
        print('Access Denied', b - a, 'attempts left')
        if(b ==0):
            print('Try again')
        continue
