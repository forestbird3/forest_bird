n=7
m=[[0]*(n+1) for i in range(n)]
i=0; j=(n-1)//2; m[i][j]=1

for k in range(2,n*n+1):
    if (k-1)%n==0: i+=1
    elif i==0: i=(n-1); j+=1
    elif j==(n-1):i-=1; j=0
    else: i-=1; j+=1
    m[i][j]=k

for i in m:                         #[0,0,0]�κ��� 3������ ǥ��
    for j in i:                     #, [] �κ��� ����
        w='{0:>4d}'.format(j)
        print(w,end=' ')            #�Ϸķ�����
    print()                         #�ٹٲ�
    