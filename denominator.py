n=int(input())
a=1
for i in range(1,n//2+1):
    if n%i==0:
        a=a+1
print(a)
