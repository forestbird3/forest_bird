print('구구단 몇단을 계산할까요? (1~9)')
x=int(input())
while 1 <= x <= 9:
    if 1<= x <= 9:
        for i in range(1,10):
            print('구구단 ', x, '단을 계산합니다.')
            result = x * i
            print(x,'x', i, '=', result)
    else:
        print('구구단 몇 단을 계산할까요? (1~9)')
else x == 0 and x > 9:
    print('구구단 게임을 종료합니다.')
