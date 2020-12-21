m=int(input())
n=0
for c10 in range(m//10+1):
    for c50 in range(m//50+1):
        for c100 in range(m//100+1):
            for c500 in range(m//500+1):
                if c10*10+c50*50+c100*100+c500*500==m:
                    n=n+1
print(n)
