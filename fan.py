y,m,d=map(int,input().split())
ty,tm,td=map(int,input().split())
total=(y+m+d+ty+tm+td)
if total%10==0:
    advice='lucky day'
else:
    advice='be careful'
print(advice)
