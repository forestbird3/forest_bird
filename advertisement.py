o,x,c=map(int,input().split())
if o>(x+c):
    judge='advertise'
elif o==(x+c):
    judge='does not matter'
else:
    judge='do not advertise'
print(judge)
