def dfs(i):
    v[i]=1
    print(i,end='')
    for j in range(1,n+1):
        if adj[i][j]==1 and v[j] ==0:
            dfs(j)


#driver code
n=6
adj=[[0,0,0,0,0,0,0],
     [0,0,1,0,1,0,0],
     [0,1,0,1,1,1,0],
     [0,0,1,0,1,0,0],
     [0,1,1,1,0,0,1],
     [0,0,1,0,0,0,1],
     [0,0,0,0,1,1,0]]
v=[0 for i in range(n+1)] #배열의 초기화(값)
print(v)
dfs(1)