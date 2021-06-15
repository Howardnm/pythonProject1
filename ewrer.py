import random
txt = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ls = list(txt)
for i in range(10):
    password = ""
    for j in range(8):
        password += random.choice(ls)
    print(password)
