import keyword
def Is_legalword(s):  # 判断是否是合法字符（数字、字母或下划线）
    for key in s:
        if not key in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_':
            return False
    return True
def Is_legal(s):
    if s[0] == '_' or s[0].isalpha():  # 开头为字母或下划线
        if keyword.iskeyword(s):  # 判断是否为Python保留关键字
            return False
        elif Is_legalword(s):
            return True
        else:
            return False
    else:
        return False
print("请输入Python标识符：")
line = input()
print(Is_legal(line))







