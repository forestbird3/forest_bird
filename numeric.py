n=10000                #기본 조건부
left=0

for i in range(1,n+1):  #작용부
    left+=i-1
    right=0
    for j in range(i+1,i*2):
        right+=j
        if left>right:
            continue
        if left<right:
            break
        print(i)