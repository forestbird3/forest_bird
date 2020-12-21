#1교시
#a=3
#print(type(a))
#print(id(a))
#print(dir(a))
#b=a.__add__(5)
#print(b)

#2교시
for i in 'abc': #iterable object를 index 0번부터 대입
    if i=='b':continue 
    print(i) #index 번호 0번 출력 / 다음 번호로 위로 다시 올라감
    print(i*5) #없을시 중지 / roop 빙글빙글 돌아가면서 반복 실행
else: # : 다음에는 처리해야할 문장들(1줄이상)
    print('end') 
             # 문장들 = suite ( 들여쓰기로 표현 )
             # 모든 들여쓰기가 같으면 실행이 됨 / 하지만 잘 보이기위해서 4칸으로 설정
             # F7번을 통해서 디버깅 할 수 있음. 수정할 때 사용. 처리과정분석. 내용수정
             #for 문을 강제로 벗어남. for문은 else 까지 포함.
             # 중첩 for문 break를 걸시 1개의 for문만 걸림
             # continue는 건너뛰고 진행