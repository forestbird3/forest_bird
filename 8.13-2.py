a=[9,5,4,3,2,6,156,441213,52,1]
x=7
msg=('no','yes')
m=0
idx=-1
for i,v in enumerate(a): #index 값과 아이템값을 i와 v에 저장
    if x == v: #x의 값과 v(a의 아이템 값)의 값이 같을때
        m=1 #m값을 1로 표현
        break #for루프탈출
    else: i=idx #x의 값과 v(a의 아이템 값)의 값이 다를때 i를 idx의 값으로 표현
print(i, msg[m])