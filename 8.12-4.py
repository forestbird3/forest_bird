from turtle import *
def tree(n, a, h, w):
    if n==0: return
    setheading(a)
    x, y=position()
    width(w)
    fd(h)
    tree(n-1, a-90, h*0.7, w*0.5)
    tree(n-1, a+90, h*0.7, w*0.5)
    goto(x,y)

#driver code
setup(800,800)
speed(10)
pencolor('black')
up(); setx(0); sety(-300); down()
tree(11, 90, 200, 3)
done()