di=[0,1,1,1,0,-1,-1,-1]                 # 열
dj=[1,1,0,-1,-1,-1,0,1]                 # 행
g = int(input())
n = int(input())                        # board의 크기
next = [[0]*(n+2) for i in range(n+2)]
now = [[0]*(n+2) for i in range(n+2)]   # board의 크기를 2차원 배열로 만듬
data = ','.join(iter(input, ''))        #iter : 키보드에 입력된 것을 반복, '' <- iter 함수에 탈출 조건 == 전체는 string문으로 되어있고 그안에 ','(콤마)로 정의
for i in data.split(','):               # ','(콤마) 기준으로 분할                               
    r,c=map(int,i.split())
    now[r][c]=1
for cycle in range(g):
    if cycle==g-1:
        life=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                life+=now[i][j]
        break
    for i in range(1,n+1):
        for j in range(1,n+1):
            life=0
            for k in range(8):
                life+=now[i+di[k]][j+dj[k]]
            next[i][j]= (life==3) or (now[i][j]==1 and life==2)
    for i in range(1,n+1):
        for j in range(1,n+1):
            now[i][j]=next[i][j]

print(life)