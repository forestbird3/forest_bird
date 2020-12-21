m=['odd','even']
a,b=map(int,input().split())
at,bt=(a%2==0),(b%2==0)
ar=1-(at != bt)
mr=(at or bt)
add='{0} + {1} = {2}'.format(m[at], m[bt], m[ar])
mul='{0} * {1} = {2}'.format(m[at], m[bt], m[mr])
print(add)
print(mul)
