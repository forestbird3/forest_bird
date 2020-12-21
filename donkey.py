x,y=map(int,input().split())
t=100
for i in range(1,t):
    for j in range(t-1):
        a=i+x==y*(j-x)
        b=i-x==j+x
        if a and b:
            m=i
            d=j
            break
print(m,d)
