c,m=map(int,input().split())
n=0
while c*4<m:
    m=m+1
    c=c+1
    n=n+1
    if c*4>m:
        break
print(n)
