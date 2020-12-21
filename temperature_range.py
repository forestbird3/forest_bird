t=list(map(float,input().split()))
for i in range(len(t)-1):
    s=round(t[i+1]-t[i],1)
    print(s)
