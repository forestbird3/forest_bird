def finding(i,j):
    global p,counter
    maze[i][j]=1
    path[p][0],path[p][1]=i,j
    p+=1
    if i==ei and j==ej:
        counter+=1
        print('path:',counter)
        print(path[:p])
    for k in range(4):
        ti,tj=i+di[k],j+dj[k]
        if maze[ti][tj]==0: finding(ti,tj)
    p-=1
    maze[i][j]=0
    
maze=[[2,2,2,2,2,2,2,2,2],
      [2,0,0,0,0,0,0,0,2],
      [2,0,2,2,0,2,2,0,2],
      [2,0,2,0,0,2,0,0,2],
      [2,0,2,0,2,0,2,0,2],
      [2,0,0,0,0,0,2,0,2],
      [2,2,0,2,2,0,2,2,2],
      [2,0,0,0,0,0,0,0,2],
      [2,2,2,2,2,2,2,2,2]]

si,sj,ei,ej,p,counter=1,1,7,7,0,0
di=[0,1,0,-1]
dj=[1,0,-1,0]
node=7
path=[[0,0] for i in range(node*node)]
finding(si,sj)