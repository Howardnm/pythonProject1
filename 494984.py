r="7799552267"
if r[0:2] in ["77"]:
    print("1",end=" ")
    print(456)
print(list(range(10)))
print("{}123{}456{}".format("x","y","z"))
print("{0:*<30}123{1}456{2}".format("x","y","z"))
print(int("1001",2))
print(int("0xf",16))
print(str(4.5))
print(hex(15))
print(oct(15))
print(r[0:-2])
print(r[-2])
print(18//4)
print(18%4)
def we(x):
    return x,x**x
print(we(3))
rt = complex(4,3)
print(rt)
rf = 3+4j
print(rf)
print(pow(2,5))
txt = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ls = list(txt)
print(ls)
print("BOOK".lower())
print("book".upper())
print("b#g#f".split("#"))
print("book".count("o"))
print("book".replace("o","y"))
print("book".center(6,"-"))
print("book".strip('b'))
print("-".join("book"))
print(type(1))
print(type("sad"))
print(type(1.1))
fg='世界那么大，我想去看看'
print(fg[7:-3])
ls=['132','6556','548']
print(ls)
print(tuple(ls))
lt=ls[0:]
print(lt)
ld=['465780','649463',('67','155')]
print(ld[2])
lp=('465780','649463',ls)
print(lp[2])
ld+=lp
print(ld)
ld[0]=0
print(ld)
del ld[::2]
print(ld)
lq={'132','6556','548'}
print(lq.pop())
lq.add('a')
print(lq)
fg=['a','a','a']
fg.remove("a")
print(fg)
d={'a1':'1','b1':'2','c1':'3'}
d.popitem()
print(d)
d.pop('b1')
print(d)
t=("cat","dog","tiger","human")
t=t[::-1]
print(t)
