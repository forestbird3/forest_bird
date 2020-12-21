c,a,n,charge=map(int,input().split())
for i in range(n+1):
    cm=i*c
    am=(n-i)*a
    if cm+am==charge:
        break
print(i)
