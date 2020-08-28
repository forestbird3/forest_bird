from turtle import *
def tree(n, a, h, w):
    if n==0: 
        dot(15, 'pink')
        return
    setheading(a)
    x, y=position()
    width(w)
    fd(h)
    tree(n-1, a-25, h*4/5, w/2)
    tree(n-1, a-45, h*4/5, w/2)
    tree(n-1, a+15, h*4/5, w/2)
    tree(n-1, a+55, h*4/5, w/2)
    tree(n-1, a+85, h*4/5, w/2)
    goto(x,y)


#driver code
setup(800,800)
speed(10)
pencolor('black')
up(); setx(0); sety(-300); down()
tree(6, 90, 200, 30)
done()