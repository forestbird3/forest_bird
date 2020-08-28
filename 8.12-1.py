from turtle import *
def box(n,x,y,r):
    if n == 0: return
    
    up(); goto(x-r,y-r); down()
    goto(x+r, y-r); goto(x+r, y+r); goto(x-r, y+r); goto(x-r, y-r);
    
    box(n-1,x-r,y-r,r//2)
    box(n-1,x+r,y-r,r//2)
    box(n-1,x+r,y+r,r//2)
    box(n-1,x-r,y+r,r//2)
    
#driver code
setup(800,800)
speed(30)
pencolor("blue")
width(3)
box(5,0,0,100)
done()