di=[0,1,1,1,0,-1,-1,-1]
dj=[1,1,0,-1,-1,-1,0,1]
m=['.','@']
n=10
next=[[0]*(n+2) for i in range(n+2)]
now=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for cycle in range(3):
    for i in range(1,n+1):
        for j in range(1,n+1): 
            print(m[now[i][j]],end=' ')
        print()
    for i in range(1,n+1):
        for j in range(1,n+1):
            s=0
            for k in range(8):
                s+=now[i+di[k]][j+dj[k]]
            next[i][j]=(now[i][j]==0 and s==3) or (now[i][j]==1 and (s==2 or s==3))
    #for i in range(n+2):
        #for j in range(n+2):
            #now[i][j]=next[i][j]
    print('\n')
                #next[i][j]=1
            #else: next[i][j]=0
            #print(m[next[i][j]],end=' ')
        #print()
#�Ӽ����ٺ��ٺ��ٺ��ٺ��ٺ��ٺ��ٺ��ٺ�
#��û�̸�û�̸�û�̸�û�̸�û�̸�û��
#�޷ո޷ո޷ո޷ո޷ո޷ո޷ո޷ո޷�
#���� �ѹ�����?
#�߰��ƾƾƤ���~~~~ ������Ű���ӵf�O�O���O��Ű��Ű
"""�١ڡ١� ���� ���Դ� ��� �١ڡ١�"""