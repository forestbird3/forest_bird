import time
start=time.time()
data=map(int,input())
bound=1000000
arr=[0]*(bound)
arr[1]=1
for i in range(2,bound):
    n=i
    cycle=1
    while n!=1:
        if n%2!=0:
            n=3*n+1
            cycle+=1
        n//=2
        cycle+=1
        if n<i:
            arr[i]=cycle+arr[n]-arr[1]
            break

for r in data:
    print(r)
    p,q=map(int,r.split())
    a,b=p,q
    if a>b:
        a,b=b,a
    m=max(arr[a:b+1])
    print(p,q,m)
    
end=time.time()
run=end-start
print(run)
    