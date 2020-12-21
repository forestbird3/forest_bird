n,m=map(int,input().split())
for c1 in range(1,n+1):
    c5=n-c1
    if ((c1*100)+(c5*500))==((c1*500)+(c5*100-m)):
        break
print(c1,c5)
