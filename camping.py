h=map(float,input().split())
c=float(input())
for i in h:
    if c>i:
        a='CRASH '+str(i)
        break
else:
    a='NO CRASH'
print(a)
