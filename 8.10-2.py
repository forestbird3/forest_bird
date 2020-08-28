def put(n):
    if n==0: return
    return n+put(n-1)

t=put(10)
print(t)