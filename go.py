n,s=map(int,input().split())
t=0
for i in range(0,n+1):
    for j in range(0,n-i+1):
        if (i*5)+(j*10)==s:
            t=t+1
print(t)
