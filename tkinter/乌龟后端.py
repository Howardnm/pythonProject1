from turtle import *
import random  # 引用随机函数
import time  # 引用时间函数
Screen().setup(600, 600, 100, 100)  # 窗口大小
delay(0)  # 0-10 画笔速度
speed(0)
hideturtle()  # 隐藏光标
pensize(5)  # 笔粗
colors = ["blue", "black", "deeppink", "orange", "green"]  # 颜色列表
name = ["操😂", "孙😘", "霍😜", "阮😝", "钟😄"]  # 成员名称
name_size = [30, 30, 30, 30, 30]  # 成员图标大小
name_y = [40, 40, 40, 40, 40]  # 成员起跑线误差
name_x = [0, 0, 0, 0, 0]  # 成员起跑线横坐标位置
length = 460  # 成员需要跑的总路程
rm = {}  # 建立每只马的总路程列表
rm1 = {}  # 建立随机数列表
for i in range(5):  # 5个成员
    rm['r' + str(i)] = 0  # 每个成员的起跑线归零
for i in range(10000000):  # 回合循环
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
# 1、提取最大值变量名 2、字符串转整数 3、提取成员名字 4、打印
done()
