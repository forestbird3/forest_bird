a=[9,5,4,3,2,6,156,441213,52,1]
x=7
for i in a:
    if x == i: #x의 값과 i(a의 아이템값)과 같을 때
        print('yes')
        break #for루프 탈출
else: #x의 값과 i(a의 아이템값)과 다를때
    print('no')