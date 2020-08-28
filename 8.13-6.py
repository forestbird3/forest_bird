def isBalence(s):
    n=0
    for i in s:
        if i=='(':n+=1
        else: n-=1
        if n<0: return 0
    if n==0: return 1
    else: return 0

def par(n,s=''):
    if n==0:
        if isBalence(s): print(s)
        return
    par(n-1,s+'(')
    par(n-1,s+')')


#driver code
n=2
par(n*3)