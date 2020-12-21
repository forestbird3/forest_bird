n=int(input())
a=0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        for k in range(j+1,n+1):
            if i<j<k:
                a=a+1
print(a)
