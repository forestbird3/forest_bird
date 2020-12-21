m=map(float,input().split())
f=map(float,input().split())
l=0.0
for i in m:
    if l<i:
        l=i
for i in f:
    if l<i:
        l=i
print(l)
