a,b,c=1000,500,50
m,n=map(int,input().split())
for i in range(m//a+1):
    for j in range(m//b+1):
        for k in range(m//c+1):
            if ((i*a)+(j*b)+(k*c)) == m and (i+j+k==n):
                ti=i
                tj=j
                tk=k
print(ti,tj,tk)
