
for i in 'good':
    print(i,end=' ') #end�� �������� �Ҵ�ǰ� ��µǰ� ''�ȿ��ִ°��� �߰��ϰ�, �ٹٲ��� �����ʰڴ�.
    
s=[1,3,5]
for i in s:
    print(i, end=' ')
    
for i in range(0,5,1): #range�� ������ �� ���� ��µ� / 3��°�ڸ��� ���� / ���۰� 0�� ���� >>>> range(5) �� ����
    print(i, end=' ')

a=range(5) #generate(������) 
print(a)
for i in a:
    print(i, end=' ')

s=[[1,2,3],[11,22,33],[111,333,555]] #����list ���� /
for x,y,z in s: #unpacking �ϴ� �۾�
    print(x, y, z)

for i in range(0,10,2):
    print(i, end=' ')
    
s=[1,3,5]
for i,x in enumerate(s): #index�� value ���ÿ� �ݺ� ������ �Ҵ�
    print(i,x)
   
s=[1,3,5,7,9]
t=[2,4,6,8]
a=zip(s,t) #s�� t�� ���ļ� �ϳ��� �������� ���� ( ������ ¦�� �¾ƾ� �����ǰ� �ϳ��� ������ �������� ��µ��� ����)
for x,y in a:
    print(x,y)
