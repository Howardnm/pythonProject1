def f(m,n):
    r=m%n
    while(r!=0):
        m=n
        n=r
        r=m%n
    return n
print(f(n=32,m=18))