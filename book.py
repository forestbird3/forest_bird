p=map(int,input().split())
b,bl=0,0
for i in p:
    if i>=49:
        b=b+1
    else:
        bl=bl+1
print(b,bl)
