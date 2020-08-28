print('구구단 몇 단을 계산할까요? (1~9)')
print('단, 0을 입력하면 프로그램이 종료됩니다.')
variable = int(input())
print('구구단 ', variable,'단을 계산합니다.')
if 0 < variable  and variable < 10:
    for i in range(1,10):
        result = variable * i
        print(variable, 'X', i, '=', result)
else:
    print('프로그램이 종료됩니다.')
