money,age,year=map(int,input().split())
r=(money*10.0)/(age*year)
if r>=2.0:
    judge='A'
elif r>=1.0:
    judge='B'
elif r>=0.5:
    judge='C'
else:
    judge='D'
print(judge)
