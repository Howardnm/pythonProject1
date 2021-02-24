#!/usr/bin/python
# -*- coding: UTF-8 -*-

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print (counter)
print (miles)
print (name)

a, b, c = 1, 2, "john"
var1 = 1
var2 = 10
print(var2,var1)
del var1


str = 'Hello World!'

print (str)  # 输出完整字符串
print (str[0])  # 输出字符串中的第一个字符
print (str[2:5])  # 输出字符串中第三个至第六个之间的字符串
print (str[2:])  # 输出从第三个字符开始的字符串
print (str * 2)  # 输出字符串两次
print (str + "TEST")  # 输出连接的字符串

print(name.lower())  #变小写
print(name.upper())  #变大写
print(name.isupper()) #真假值
print(name.upper().isupper())
print(len(str)) #数数
print(str.index("l")) #索引位置
print(str.index("Wor"))
print(str.replace("Hello","good morning"))  #替换
