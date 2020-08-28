def dfs(i):
    v[i]=1
    print(i,end=' ')
    for j in range(1,n+1):
        if adj[i][j]==1 and v[j] ==0:
            dfs(j)
            

#driver code
n=int(input())
adj=[[0 for i in range(n+1)] for j in range(n+1)]
s='\n'.join(iter(input,''))
for i in s.split('\n'):
    row, col = map(int,i.split())
    adj[row][col]=1
    adj[col][row]=1
    
for i in range(n+1):
    print(adj[i])

v=[0 for i in range(n+1)]
dfs(1)