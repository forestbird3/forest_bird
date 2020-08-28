def conv(n, base, s):
    if n == 0: return s
    return conv(n//base, base, a[n%base]+s)

a='0123456789ABCDEF'
n,base=255,16
s=conv(n,base,'')
print(s)

"""=================================================================="""

#def conv(n,s):
    #if n==0: return s
    #return conv(n//base,a[n%base]+s)

#a='0123456789ABCDEF'
#n,base=255,16
#s=conv(n,'')
#print(s)