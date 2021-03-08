from turtle import *  # 缺点：有可能会重名
Screen().setup(650, 350, 200, 200)
penup()
fd(-250)  # fd前进 bk后退 circle(r,angle)做圆
pendown()
pensize(25)
pencolor("purple")
seth(-40)  # 旋转到指定角度，left和right是转向
for i in range(4):
    circle(40, 80)
    circle(-40, 80)
circle(40, 80/2)
fd(4)
circle(16, 180)
fd(40 * 2/3)
done()