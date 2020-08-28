def exp(n,s):
    if n==eps:
        s=s+str(n)
        if eval(s) == make: print(s) #eval : str을 int 형태로 바꾸어 계산
        return
    
    for i in op:
        exp(n+1,s+str(n)+i)
    
#driver code
op=['+','-','*','/','']
eps=9
make=100
exp(1,'')