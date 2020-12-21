a,b=map(int,input().split())
m1=15000
m2=20000
if a+b>=20:
    total=((m1*a)+(m2*b))*90//100
else:
    total=(m1*a)+(m2*b)
print(total)
