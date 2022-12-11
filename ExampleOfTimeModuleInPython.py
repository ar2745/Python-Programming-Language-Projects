import time

login1 = time.time()
time.sleep(4)

message1 = time.time()
time.sleep(7)

logout1 = time.time()
time.sleep(12)

login2 = time.localtime(login1)
message2 = time.localtime(message1)
logout2 = time.localtime(logout1)

login = time.asctime(login2)
message = time.asctime(message2)
logout = time.asctime(logout2)

print(login)
print(message)
print(logout)