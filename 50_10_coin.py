n,c=map(int,input().split())
for i in range(1,n):
    if (i*50)+((n-i)*10)==c:
        break
print(i,(n-i))
