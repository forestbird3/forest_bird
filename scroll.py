n=int(input())
s=input()
for i in range(n):
    print(s)
    s=s[1:]+s[0]
