a,b=map(int,input().split())
n=0
for i in range(a,b+1):
    k,j=i,1
    while k:
        k=k//10
        j=j*10
    if (i*i-i)%j==0:
        n=n+1
print(n)
