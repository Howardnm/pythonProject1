from turtle import *
bgcolor('black')
delay(0)
speed(0)
colors = ["purple", "green", "yellow", "orange", "red"]
fds = [400, 300, 250, 200, 160]
def sbsb(sb):
    color(colors[sb])
    fd(fds[sb])
    dot(6)
    bk(fds[sb])
    right(2)
for x in range(180):
    if x % 2 == 0:
        sbsb(0)
    elif x % 3 == 0:
        sbsb(1)
    elif x % 5 == 0:
        sbsb(2)
    elif x % 7 == 0:
        sbsb(3)
    else:
        sbsb(4)
done()
