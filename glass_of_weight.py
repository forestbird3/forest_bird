a1,a2,b1,b2,w=map(int,input().split())
for i in range(1,w):
    for j in range(1,i):
        if (a1*i)+(a2*j)==w and (b1*i)+(b2*j)==w:
            l=i
            s=j
print(l,s)
