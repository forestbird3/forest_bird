a,b,m=map(int,input().split())
n=0
while a != b*2:
    a=a-m
    b=b-m
    if b<=0:
        n=-1
        break
    n=n+1
print(n)
