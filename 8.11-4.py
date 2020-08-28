from turtle import *
from math import sin,cos
setup(800,800)
speed(1)
pencolor('red')
width(5)
p=3.1459265
r=50
up(); goto(r,0); down()
for i in range(0, 360*2+5, 360*2//5):
    
    a=i*p/180
    
    x=r*cos(a)
    y=r*sin(a)
    
    goto(x,y)
    
done()