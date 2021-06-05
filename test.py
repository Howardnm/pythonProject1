weekStr = "星期一星期二星期三星期四星期五星期六星期日"

str  = input("请输入星期数字(1-7)：")

#*****FOUND*****

weekId = int(str)

#*****FOUND*****

pos = weekId * 3

#*****FOUND*****
print(weekStr[pos-3:pos])