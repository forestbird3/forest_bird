day=[31,28,31,30,31,30,31,31,30,31,30,31]
table=[[0]*42 for i in range(12)]
year,divide=map(int,input().split()) #input ���� �̿��ؾ��ҵ�
month=dict(zip(range(12),'Jan Feb Mar Apr May Jun Jul Agu Sep Oct Nov Dec'.split()))
week='Sun  Mon  Tue  Wed  Tur  Fri  Sat       '
day[1]=day[1]+(year%4==0 and year%100 != 0) or (year%400==0)
y=year-1 #����ϰ� ���� �⵵ ���⵵���� ���
weekday=((365*y)+(y//4)-(y//100)+(y//400)+1)%7 #����ϰ� ���� ��¥�� 1��1���� �ε�����
for i in range(12):
    for j in range(day[i]):
        table[i][j+weekday]=j+1
    weekday=(j+weekday+1)%7
for i in range(0,12,divide): #��,2������ ����
    print(month[i],month[i+1])
    print(week*divide)
    for j in range(0,42,7): #�������� 42���� 7��
        for k in range(i,i+divide):  #2������ ǥ���� �ؾߵǼ� ������ ù��°�־� ǥ��
            for l in range(j,j+7):
                w='{:3d}'.format(table[k][l])#1�ֿ� 7���� ���� ������ 7ĭ
                print(w,end='  ')
            print(' '*4,end='')
        print()
    print('\n'*2)