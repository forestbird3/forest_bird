n=int(input())
r=map(float,input().split())
m=1000.0
for i in r:
    if m>i:
        m=i
print(m)
