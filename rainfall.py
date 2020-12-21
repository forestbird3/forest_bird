n=int(input())
max, min=0.0, 10000.0
for i in range(n):
    r=float(input())
    if max<r:
        max=r
    if min>r:
        min=r
range=round(max-min,1)
print(range)
