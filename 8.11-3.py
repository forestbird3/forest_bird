from turtle import *
from math import sin,cos
setup(800,800)
speed(20)
pencolor('red')
width(5)
p=3.1459265
up(); goto(-360,0); down()
for i in range(-360, 360, 5):
    
    r=p*i/180
    
    s=150*sin(2*r)*cos(r/2)
    goto (i, s);pencolor('black')
    #setx(i); sety(s); dot(10,'red')
    
    
    c=300*cos(r/4)*sin(r*3)
    goto (i, c);pencolor('yellow')
    #setx(i); sety(c); dot(10,'blue')
    

print(s, c)
