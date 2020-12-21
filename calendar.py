day=[31,28,31,30,31,30,31,31,30,31,30,31]
table=[[0]*42 for i in range(12)]
year,divide=map(int,input().split()) #input 값을 이용해야할듯
month=dict(zip(range(12),'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()))
week='Sun Mon Tue Wed Thu Fri Sat     '
day[1]=day[1]+(year%4==0 and year%100 != 0) or (year%400==0)
y=year-1 #계산하고 싶은 년도 전년도까지 계산
weekday=((365*y)+(y//4)-(y//100)+(y//400)+1)%7 #계산하고 싶은 날짜의 1월1일의 인덱스값
cycle=0
print(year,'calendar')
for i in range(12):
    for j in range(day[i]):
        table[i][j+weekday]=j+1
    weekday=(j+weekday+1)%7
for i in range(0,12,divide): #월,2단으로 나눔
    for x in range(0,divide+1):
        z='{0:<31}'.format(month[i+x])
        cycle=cycle+1
        if cycle==12%divide:
            print(z,end='')
    print('\n',week*divide)
        for j in range(0,42,7): #각월마다 42개씩 7줄
            for k in range(i,i+divide):  #2단으로 표현을 해야되서 각월의 첫번째주씩 표현
                for l in range(j,j+7):
                    w='{:3d}'.format(table[k][l])#1주에 7개씩 들어가기 때문에 7칸
                    if w=='  0':
                        w='  -'
                    print(w,end=' ')
                print(' '*4,end='')
            print()
        print('\n'*2)

