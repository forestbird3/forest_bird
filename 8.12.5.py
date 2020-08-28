from turtle import *
from math import *
from random import *
def boxtree(n,x,y,a,w):
    if n==0: return
    setheading(a)
    up(); goto(x,y); down()
    c=randint(0,6)
    color(r[c])
    begin_fill()
    for i in range(4):
        fd(w)
        lt(90)
    end_fill()
    tw=w/sqrt(2)
    ta=radians(a-135)
    boxtree(n-1,x+tw*cos(ta),y+tw*sin(ta),a-45,tw)
    #ta=radians(a-45)                                            #drogon curve
    #boxtree(n-1,x+tw*cos(ta),y+tw*sin(ta),a-45,tw)      
    ta=radians(a-45)
    boxtree(n-1,x+tw*cos(ta),y+tw*sin(ta),a+135,tw)        
    #ta=radians(a-45)
    #boxtree(n-1,x+2*tw*cos(ta),y+2*tw*sin(ta),a+45,tw)

#driver code
setup(800,800)
r=['red','blue','green','yellow','purple','pink','orange']
color('red')
pencolor('green')
width(3)
speed(30)
boxtree(8,0,-200,180,200)
done()