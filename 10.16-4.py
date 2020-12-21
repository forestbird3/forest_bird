n=1000000
f,s=1,0
for i in range(1,n+1):
    s+=f/(2*i-1)
    f=-f
print(4*s)