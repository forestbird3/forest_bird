
for i in 'good':
    print(i,end=' ') #end는 아이템이 할당되고 출력되고 ''안에있는것을 추가하고, 줄바꿈을 하지않겠다.
    
s=[1,3,5]
for i in s:
    print(i, end=' ')
    
for i in range(0,5,1): #range는 끝에서 앞 까지 출력됨 / 3번째자리는 보폭 / 시작값 0은 생략 >>>> range(5) 와 같다
    print(i, end=' ')

a=range(5) #generate(생성자) 
print(a)
for i in a:
    print(i, end=' ')

s=[[1,2,3],[11,22,33],[111,333,555]] #이중list 구문 /
for x,y,z in s: #unpacking 하는 작업
    print(x, y, z)

for i in range(0,10,2):
    print(i, end=' ')
    
s=[1,3,5]
for i,x in enumerate(s): #index와 value 동시에 반복 변수에 할당
    print(i,x)
   
s=[1,3,5,7,9]
t=[2,4,6,8]
a=zip(s,t) #s와 t를 합쳐서 하나의 아이템을 생성 ( 서로의 짝이 맞아야 생성되고 하나라도 없으면 아이템이 출력되지 않음)
for x,y in a:
    print(x,y)
