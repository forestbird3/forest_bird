def euclid(a,b):
    if b==0: return a
    return euclid(b,a%b)

m=[4, 8, 34]
lcm=gcd=m[0]
for i in m[1:]:
    gcd=euclid(gcd,i)
    lcm*=i//euclid(lcm,i)
print(gcd, lcm)