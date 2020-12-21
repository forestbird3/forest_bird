n=int(input())
x=1
while (x/5)+(x/3)+(3*((x/3)-(x/5)))+n != x:
    x=x+1
    if (x/5)+(x/3)+(3*((x/3)-(x/5)))+n == x:
        break
print(x)
