# 闰年的条件：能被4整除且不能被100整除或能被400整除
def functionl(year, month, day):  # 计算给定日期是哪一年的第几天
    leap_year=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    no_leap_year=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        result=sum(leap_year[:month - 1]) + day
    else:
        result=sum(no_leap_year[:month - 1]) + day
    return result
def main():
    year, month, day=eval(input("年,月,日:"))
    result=functionl(year, month, day)
    print("{}年{}月{}日是这一年的第{}天".format(year, month, day, result))


main()

