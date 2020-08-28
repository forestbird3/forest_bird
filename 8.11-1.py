from turtle import *
setup (1000, 1000)
up()
goto(-150,-150)
down()
speed(9)
pencolor('green')
width(3)
for i in range(3, 11):
    for n in range(i):
        fd(100)
        lt(360/i)
done()