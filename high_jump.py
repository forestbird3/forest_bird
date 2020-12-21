n=int(input())
s=map(int,input().split())
t=0
for i in s:
    if i>=n:
        t=t+1
print(t)
