from turtle import *
def ruller(n, left, right, h):
    if n == 0: return
    x0=(left+right)/2
    y0=0
    x1=x0
    y1=y0+h
    up(); goto(x0,y0); down(); goto(x1,y1);
    dot(10,'black')
    
    ruller(n-1,x0,right,h*0.8)
    ruller(n-1,left,x0,h*0.8)
    

#driver code
setup(800, 800)
speed(1)
pencolor('green')
width(5)
ruller(5,-300,300,200)
ht()
done()