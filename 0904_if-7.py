msg=('no','three','two','one')
a,b,c,=3,3,3
x=0
if a+b>c and a+c>b and b+c>a:
    if a==b==c: x=1
    elif a==b or b==c or c==a: x=2
    else: x=3
print(msg[x])