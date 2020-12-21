n=int(input())
s=map(int,input().split())
max,min=0,100
for i in s:
    if max<i:
        max=i
    if min>i:
        min=i
range=max-min
print(range)
