a,b,c,d=map(int,input().split())
t=a+b+c+d
if t==1:
    t='A'
elif t==2:
    t='B'
elif t==3:
    t='C'
elif t==4:
    t='E'
else:
    t='D'
print(t)
