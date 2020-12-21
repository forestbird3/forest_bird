'''
a,b,c=map(float,input().split())
if a==b==c:
    answer='regular triangle'
if a==b or b==c or a==c:
    answer='isosceles triangle'
if a != b and a != c and b != c:
    answer='scalene triangle'
print(answer)
'''
a,b,c=map(float,input().split())
tri=['no','regular','isoceles','scalene']
x=0
if (a+b)>c and (a+c)>b and (b+c)>a:
    if a==b==c:
        x=1
    elif a==b or b==c or c==a:
        x=2
    else:
        x=3
print(tri[x])
