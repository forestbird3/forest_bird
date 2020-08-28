a='0123456789ABCDEF'
n,base=123456789,16
s=''
while n != 0:
    q = n // base
    r = n % base
    s = a[r]+s
    n = q 

print(s)

#n,base=13,2
#s=''
#while n != 0:
    #n,r = divmod(n,base)
    #s = str(r)+s
#print(s) 