def printentry():
    var2.set(var1.get())
from Tkinter import *
root=Tk()
var1=StringVar()
Entry(root,textvariable=var1).pack()
Button(root,text="print entry",command=printentry).pack()
var2=StringVar()
Label(root,textvariable=var2).pack()
root.mainloop()