h,m=map(int,input().split())
t=45
if m-t<0:
    h=h-1
    m=60-abs(m-t)
    if h<0:
        h=23
print(h,m)
