di=[0,1,1,1,0,-1,-1,-1]                 # ��
dj=[1,1,0,-1,-1,-1,0,1]                 # ��
g = int(input())
n = int(input())                        # board�� ũ��
next = [[0]*(n+2) for i in range(n+2)]  # ���� ����
now = [[0]*(n+2) for i in range(n+2)]   # �� ����

data = ','.join(iter(input, ''))        #iter : Ű���忡 �Էµ� ���� �ݺ�, '' <- iter �Լ��� Ż�� ���� == ��ü�� string������ �Ǿ��ְ� �׾ȿ� ','(�޸�)�� ����
for i in data.split(','):               # ','(�޸�) �������� ����                               
    r,c=map(int,i.split())
    now[r][c]=1

for cycle in range(g):
    if cycle == g-1:                    # cycle���� 0���� ������ 0,1,2 3���� ����
        life = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                life += now[i][j]
        break

    for i in range(1, n+1):
            for j in range(1, n+1):
                life = 0
                for k in range(8):
                    life += now[i+di[k]][j+dj[k]]
                    next[i][j] = (life == 3) or (now[i][j] == 1 and life == 2)     # ����ü�� 3�̸� ���밡 �ְ�, ����ü�� 1�̰� �ֺ��� 2�̸� �ִ�
    for i in range(1, n+1):
        for j in range(1, n+1): now[i][j] = next[i][j]

print(life)