def fac(n):
    if n==0: return 1
    r=n*fac(n-1)
    w="{0:d}!={1:d}".format(n, r)
    print(w)
    return r


f=fac(10)
