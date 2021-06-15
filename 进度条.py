import time
print("-A5H---")
for i in range(11):
    a = '*'*i
    b = '.'*(10 - i)
    c = (i/10)*100
    print("{:^3.0f}%[{}->{}]".format(c,a, b))
    time.sleep(0.1)
print(" --SA56-")