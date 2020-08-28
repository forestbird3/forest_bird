from turtle import *
from math import sin, cos
def cateyes(n,left,right):
    if n == 0: return
    x0=(left+right)//2
    y0=0
    r=g//2
    up(); goto(x1,y1); down();
    

#driver code
setup(1100,1100)
speed(2)
pencolor("black")
width(3)
g=500
up(); goto(0,-500); down();
circle(500)
cateyes(3,-500,500)
done()