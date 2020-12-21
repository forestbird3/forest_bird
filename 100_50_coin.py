n=int(input())
for i in range(1,n):
    j=n-i
    if ((i*100)+(j*50))==((i//2)*100)+(j*3*50):
        break
print(i,j)
