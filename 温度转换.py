print("请选择输入类型：")
print("1、摄氏度 2、华氏度")
tempstr = input("请输入:")
if tempstr in ['1']:
    c = input("摄氏度值：")
    c = (eval(c) - 32) / 1.8
    print("温度是:{:.2f}".format(c), "华氏度")
elif tempstr in ['2']:
    F = input("华氏度值:")
    F = 1.8 * eval(F) + 32
    print("温度是:{:.2f}".format(F), "摄氏度")
else:
    print("输入错误，结束")
#
