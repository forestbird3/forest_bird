def euclid(a, b):
    if b == 0: return a
    #r = a % b
    #a = b
    #b = r    
    return euclid(b,a%b)
    
a,b=12,32
mcd=euclid(a,b)
lcm=a*b//mcd
print(mcd,lcm)