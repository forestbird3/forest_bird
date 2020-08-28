print("2진수로 바꿔주는 프로그램입니다.")
print("숫자를 입력해주세요.")
decimal = int(input())
result = ''
while (decimal > 0):
    reminder = decimal % 2
    decimal = decimal // 2
    result = str(reminder) + result
print("답은 " + result + " 입니다.")
