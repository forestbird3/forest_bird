



#driver code
width, height = map(int, input(). split())
numbers = '\n'.join(iter(input,'')) #input 값에 줄바꿈으로 변수에 나눠서 대입
data=[[int(i) for i in line.split()] for line in numbers.split('\n')]
columns = data[:width]
rows = data[width:]
grid = [[0]*width for i in range(height)] #grid=[[0,]*width,]*height