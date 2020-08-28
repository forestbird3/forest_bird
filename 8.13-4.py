#bubble sort
a=[9,5,4,3,2,6,156,441213,52,1]
#a.sort()
#b=sorted(a)
n=len(a) #list aÀÇ ±æÀÌ
for i in range(n):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(n)
print(a)