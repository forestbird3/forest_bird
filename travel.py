b1,b2=40,20
s,n=map(int,input().split())
for i in range(1,n+1):
    if (i*b1)+((n-i)*b2)==s:
        break
print(i,n-i)
