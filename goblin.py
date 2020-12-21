m,n=map(int,input().split())
for i in range(n):
    m=m*2-3000
    if m<0:
        m=0
print(m)
