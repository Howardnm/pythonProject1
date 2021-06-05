from turtle import *
import random  # 引用随机函数
import time  # 引用时间函数
Screen().setup(850, 850, 0, 0)  # 窗口大小，窗口左上角位置
delay(0)  # 笔画速度
speed(0)
hideturtle()  # 隐藏光标
########################################################
# 1.2 定义烟花函数及变量
colors1 = ["purple", "green", "yellow", "orange", "deeppink"]  # 烟花颜色
fds = [350, 300, 250, 200, 160]  # 烟花长度
name1 = ['操程', '孙璐鑫', '霍信池', '阮潮龙', '钟家桐']  # 烟花成员

def yh(sb):  # 定义一个烟花花瓣开花方式的函数
    color(colors1[sb])
    fd(fds[sb])
    write(name1[sb], font=(5))
    dot(6)
    bk(fds[sb])
    right(2)

########################################################
# 1.2 定义赛跑程序变量
colors = ["blue", "lawngreen", "deeppink", "orange", "green"]  # 颜色列表
name = [" 操程\n(•‾̑⌣‾̑•)", "  孙\n(•‾̑⌣‾̑•)", "  霍\n(ó㉨ò)ﾉ", "   阮\n（´∀｀）", "  钟\n(▔▽▔)"]  # 成员名称
name_size = [20, 20, 20, 20, 20]  # 成员图标大小
name_y = [50, 50, 50, 50, 50]  # 成员起跑线误差
name_x = [-12, -13, -13, -25, -20]  # 成员起跑线横坐标位置
length = 460  # 成员需要跑的总路程
rm = {}  # 建立每个成员的总路程列表
rm1 = {}  # 建立随机数列表
for i in range(5):  # 5个成员
    rm['r' + str(i)] = 0  # 每个成员的起跑线归零

########################################################
# 2.1 开始赛跑程序
pensize(5)  # 笔粗
for i in range(1000000):  # 回合循环
    time.sleep(0.01)  # 每个回合等待0.05秒
    clear()  # 每个回合清屏
    # 画出起跑线和终点线
    pencolor(colors[3])
    pu()
    goto(-230, -230)
    pd()
    goto(230, -230)
    pu()
    goto(-230, 230)
    pd()
    goto(230, 230)
    # 每个成员走一回合随机步
    for i in range(5):
        rm1['r' + str(i)] = int(random.randint(0, 10))
        rm['r' + str(i)] = rm['r' + str(i)] + rm1['r' + str(i)]
        pencolor(colors[i])
        pu()
        goto(name_x[i] + i * 105 - 230, rm['r' + str(i)] - 230 - name_y[i])
        pd()
        write(name[i], font=("Arial Rounded", name_size[i], "normal"))
    # 其中一个成员走到终点时，立刻停止循环
    if max(rm.values()) >= length:
        break  # 停止for循环
print('每个成员的最后总路程分别为')
for i in range(5):  # 打印每个成员的总路程
    print(rm['r' + str(i)], end=' ')
print(name[int(max(rm, key=rm.get)[-1])], "赢了!!!")
# 上面打印分析：1、提取最大值变量名 2、字符串转整数 3、提取成员名字 4、打印
up()
goto(-100, -50)
write(name[int(max(rm, key=rm.get)[-1])]+"赢了!!!", font=("Arial Rounded", 30))  # 绘画谁赢了
time.sleep(3)  # 等待两秒

########################################################
# 2.2 开始画烟花
bgcolor('black')  # 设置背景为黑色
goto(0, 0)
clear()
pensize(1)
pd()
for x in range(180):  # 开始绘烟花
    if x % 3 == 0:
        yh(0)  # 调用烟花函数，并设置变量sb = 0
    elif x % 11 == 0:
        yh(1)
    elif x % 5 == 0:
        yh(2)
    elif x % 7 == 0:
        yh(3)
    elif x % 2 == 0:
        yh(4)
    else:
        yh(1)
done()
