from turtle import *
r = 100  # 半径
angle = 360
pensize(20)  # 粗细
colors = ["blue", "black", "red", "orange", "green"]  # 颜色
x = -4.8  # 水平位移校准
y = 0  # 竖直位移校准

for i in range(5):
    pencolor(colors[i])
    circle(40, 80)
    circle(-40, 80)
done()