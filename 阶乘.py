def factorial(num):
    if num == 0:
        #*****SPACE*****
        return 1
    else:
        #*****SPACE*****
        return num * factorial(num-1)
n = eval(input("请输入一个整数: "))
print(factorial(abs(int(n))))