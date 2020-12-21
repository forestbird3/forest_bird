a,d,n=map(int,input().split())
t=''
for i in range(n):
    t=t+str(a)+' '
    a=a+d
print(t)
