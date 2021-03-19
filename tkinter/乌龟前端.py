import tkinter as tk
###################################################
window = tk.Tk()
window.title('赌马')
window.geometry('500x300')
#############################
bv1 = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
cash_see=tk.StringVar()
cash = 1000
on_start = False
def startgui():
    global on_start  # 若想在函数内部对函数外的变量进行操作，就需要在函数内部声明其为global（全局）
    global cash
    global e3
    if on_start == False:
        bv1.set('状态：开始中。。。')
        #############
        import os
        os.system('python 乌龟后端.py')  # 调用turtle画板程序
        #############
        print(e3.get())
        cash = cash - eval(e3.get())
        print(cash)
        cash_see.set('钱包:{:}'.format(cash))
        bv1.set('状态：结束')
    else:
        bv1.set('状态：结束')

#############################
l1 = tk.Label(window, text='下注窗口', font=('Arial', 16))
l1.pack()
cash_see.set('钱包:{:}'.format(cash))
l2 = tk.Label(window, textvariable=cash_see, font=('Arial', 12))
l2.place(x=10, y=30)
l3 = tk.Label(window, text='本次下注金额：', font=('Arial', 12))
l3.place(x=10, y=60)
e3 = tk.Entry(window, show=None, font=('Arial', 14), width=5)  # 显示成明文形式
e3.place(x=120, y=60)
l3_1 = tk.Label(window, text='元', font=('Arial', 12))
l3_1.place(x=200, y=60)


l2 = tk.Label(window, textvariable=bv1, font=('Arial', 12))
l2.place(x=10, y=120)
b1 = tk.Button(window, text='开跑', font=('Arial', 12), width=10, height=1, command=startgui)
b1.place(x=220, y=230)
window.mainloop()

###################################################