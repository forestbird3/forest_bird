n,o,y,m,d=map(int,input().split())
w=o+y+m+(n*3)
f=d+n
t=0
while w<=f:
    w=w+3
    f=f+1
    t=t+1
    if w>f: break
print(t)
