import turtle  # 引入turtle绘图库
turtle.Screen().setup(650, 350, 200, 200)  # 画布窗口长宽，在屏幕位置
turtle.penup()  # 即pu
turtle.fd(-250)  # fd前进 bk后退 circle(r,angle)做圆
turtle.pendown()  # 即pd
turtle.pensize(25)
turtle.pencolor("purple")
turtle.pencolor(0.63, 0.13, 0.94)  # RGB
turtle.seth(-40)  # 旋转到绝对角度，left和right是转向
colors = ["blue", "black", "red", "orange", "green"]
for i in range(4):
    turtle.pencolor(colors[i])
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80 / 2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
turtle.done()  # 设置这行后，窗口不自动关闭
