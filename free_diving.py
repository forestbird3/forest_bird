a,b,c=map(float,input().split())
ratio=a/100.0
height=c
while b>0:
    height=height/ratio
    b=b-1
s=round(height)
print(s)
