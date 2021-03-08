from turtle import *
r = 100  # 半径
angle = 360
pensize(20)  # 粗细
colors = ["blue", "black", "red", "orange", "green"]  # 颜色
x = -4.8  # 水平位移校准
y = 0  # 竖直位移校准
for i in range(5):
    x = 2.4+x
    if i == 3:
        x = -3.6; y = -r
    pencolor(colors[i])
    pu()
    goto(x*r-2.4*y, y)
    pd()
    circle(r, angle)
done()
# 高分子1802霍信池