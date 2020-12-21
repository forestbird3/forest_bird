n=map(float,input().split())
m=0
for i in n:
    if i>=30:
        g=i*3000
    else:
        g=i*1200
    m=m+g
t=round(m/1000)*1000
print(t)
