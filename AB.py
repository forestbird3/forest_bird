x,y=map(int,input().split())
for a in range(1,x+1):
    b=x//a
    if a-b==y:
        add=a+b
        break
print(a,b,add)
