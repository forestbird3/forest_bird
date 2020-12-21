a=int(input())
if a%4==0:
    if a%100==0:
        if a%400==0:
            n='leap'
        else:
            n='common'
    else:
        n='leap'
else:
    n='common'
print(n)
