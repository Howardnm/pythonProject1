import turtle as tu

# 实例化一张画布。
# 也可以不用实例化，直接用 tu.setup(480,360)。
# 因为turtle会自动初始化一张画布。
scr=tu.Screen()
src=tu.getscreen()  # 获取当前的屏幕/画布
scr.setup(480, 360)
scr.delay(0)

# 实例化一支笔 pen1 用来显示坐标。
pen1=tu.Turtle()
pen1.pen(pencolor='blue', pensize=2)
pen1.up()
pen1.goto(0, 130)

# 实例化第二支笔 pen2 用来绑定事件。
pen2=tu.Turtle(shape='turtle')
pen2.pen(pencolor='red', pensize=2, fillcolor='yellow')


# 定义一个可以绑定的函数。
def cursor_x_y(event):
    """要进行坐标转换,因为 event.x, event.y 获取的坐标的原点是在
    窗口的左上角，坐标轴是这样的┌ ，而画布中的坐标原点是在画布中心└。"""
    x=event.x - 240
    y=180 - event.y
    s="鼠标坐标为:" + str(x) + "," + str(y)
    pen1.clear()
    pen1.write(s, align="center", font=("Arial", 16, "normal"))


scr.onclick(pen2.goto)  # 第一种绑定鼠标事件的方法：鼠标单击。

scr.cv.bind("<Motion>", cursor_x_y)  # 第二种绑定鼠标事件的方法：鼠标移动。
# scr.cv.bind("<Button-3>",cursor_x_y) # 右键单击。（其他可以参考tkinter的绑定）

pen2.ondrag(pen2.goto)  # 第三种是画笔绑定事件。需要注意的是：
# 此方法绑定，想要触发事件，
# 必须得鼠标单击到“小乌龟”，并拖动它。

tu.mainloop()
