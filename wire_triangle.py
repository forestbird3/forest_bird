w=int(input())
t=w//2+1
n=0
for i in range(1,t):
    for j in range(i,t):
        for k in range(j,t):
            if i+j+k==w and i+j>k:
                n=n+1
print(n)
