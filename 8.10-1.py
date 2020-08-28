#Recursive call 재귀적 호출
def strategy(n): #n=가인수
    if n==0: return #base case 탈출조건
    strategy(n-1) #inductive case 유도조건/ 자기가 끝나기전에 자신을 호출함 / 재귀
    print(n) 
    return #생략가능
    
#driver code
strategy(10) #calling define을 호출함/ 10=실인수