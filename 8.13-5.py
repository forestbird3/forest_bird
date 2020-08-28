def search(low,high):
    if low>high:    #탈출조건
        return -1
    mid=(low+high)//2   #중앙값
    if s==a[mid]:       
        return mid
    elif s < a[mid]:
        return search(low,mid-1)
    else:
        return search(mid+1, high)


#driver code
a=[5,1,9,4,6,8]
a.sort()
n=len(a) #a의 갯수
s=6 #찾고싶은 값
idx=search(0,n-1)
print(idx)